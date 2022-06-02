from django.urls import path
from django.conf import settings
from channels.routing import ProtocolTypeRouter, URLRouter

from gpsDatingApp.consumer.GameConsumer import GameConsumer
from gpsDatingApp.consumer.ChatConsumer import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path(settings.DOMAIN_SUFFIX + 'ws/game/<str:userId>/<str:gameWsVerifyCode>', GameConsumer.as_asgi()),
        path(settings.DOMAIN_SUFFIX + 'ws/chat/<str:userId>/<str:chatWsVerifyCode>', ChatConsumer.as_asgi()),
    ]),
})
