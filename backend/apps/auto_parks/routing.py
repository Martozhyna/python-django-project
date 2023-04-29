from django.urls import path

from .consumers import AutoParkConsumers

websocket_urlpatterns = [
    path('<str:room>', AutoParkConsumers.as_asgi())
]
