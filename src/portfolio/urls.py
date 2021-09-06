from django.urls import path
from . views import index, send_message

urlpatterns = [
    path('', index),
    path('send_message/', send_message)
]