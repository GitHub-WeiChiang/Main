"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.urls import path
from django.conf import settings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter

from gpsDatingApp.consumer.GameConsumer import GameConsumer
from gpsDatingApp.consumer.ChatConsumer import ChatConsumer
from gpsDatingApp.game.GameStateMachine import GameStateMachine

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    # "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": URLRouter([
        path(settings.DOMAIN_SUFFIX + 'ws/game/<str:userId>/<str:gameWsVerifyCode>', GameConsumer.as_asgi()),
        path(settings.DOMAIN_SUFFIX + 'ws/chat/<str:userId>/<str:chatWsVerifyCode>', ChatConsumer.as_asgi()),
    ]),
})

# 啟動遊戲狀態機
GameStateMachine()
