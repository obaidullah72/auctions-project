import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import auctions.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        auctions.routing.websocket_urlpatterns
    ),
})