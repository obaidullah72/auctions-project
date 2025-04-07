import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Auction, Bid
from django.contrib.auth.models import User

class AuctionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_id']
        self.auction_group_name = f'auction_{self.auction_id}'

        await self.channel_layer.group_add(
            self.auction_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.auction_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        bid_amount = data['bid']
        user_id = self.scope['user'].id

        # Save bid and update auction
        auction = await self.get_auction()
        if float(bid_amount) > float(auction.current_bid or auction.starting_bid):
            await self.save_bid(user_id, bid_amount)
            
            # Broadcast new bid to all connected clients
            await self.channel_layer.group_send(
                self.auction_group_name,
                {
                    'type': 'bid_update',
                    'bid': bid_amount,
                    'user': self.scope['user'].username
                }
            )

    async def bid_update(self, event):
        await self.send(text_data=json.dumps({
            'bid': event['bid'],
            'user': event['user']
        }))

    @database_sync_to_async
    def get_auction(self):
        return Auction.objects.get(id=self.auction_id)

    @database_sync_to_async
    def save_bid(self, user_id, amount):
        auction = Auction.objects.get(id=self.auction_id)
        Bid.objects.create(
            auction=auction,
            user=User.objects.get(id=user_id),
            amount=amount
        )
        auction.current_bid = amount
        auction.save()