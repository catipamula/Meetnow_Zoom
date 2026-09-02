<<<<<<< HEAD
from django.urls import re_path , path
from . import consumers
from .consumers import VideoChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from video_app import routing

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(routing.websocket_urlpatterns),
    }
)
websocket_urlpatterns = [
    re_path(r'ws/randomcall/(?P<room_id>\w+)/$', consumers.RandomCallConsumer.as_asgi()),
    path("ws/video/", VideoChatConsumer.as_asgi()),

=======
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/randomcall/(?P<room_id>\w+)/$', consumers.RandomCallConsumer.as_asgi()),
>>>>>>> eb2277fa704e6eef21fa833c13714f22305496f2
]
