from django.shortcuts import render, get_object_or_404
from .models import Auction

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    return render(request, 'auctions/auction_detail.html', {'auction': auction})