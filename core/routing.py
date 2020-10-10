from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.dht11.routing import websocket_urlpatterns as dht11_ws
from apps.chats.routing import websocket_urlpatterns as chats_ws

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            dht11_ws +
            chats_ws
        )
    ),
})
