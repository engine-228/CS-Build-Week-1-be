from django.shortcuts import render
from .room_models import Room
from rest_framework import viewsets
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer