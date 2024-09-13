from django.shortcuts import render
from .models import ChatRoom


def index(request):
  chatrooms = ChatRoom.objects.all()
  return render(request, 'app/index.html', {'chatrooms':chatrooms})

def chatroom(request, slug):
  chatroom = ChatRoom.objects.get(slug=slug)

  return render(request, 'app/room.html', {'chatroom':chatroom})