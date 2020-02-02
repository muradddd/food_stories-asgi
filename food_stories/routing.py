from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.urls import path
from stories.consumers import *
#
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('story/<int:pk>/', CommentConsumer),
                ]
            )
        )
    )
})