
from channels.generic.websocket import AsyncWebsocketConsumer

import json

from .models import ChatRoom



class ChatConsumer(AsyncWebsocketConsumer):

  def connect(self):
    pass