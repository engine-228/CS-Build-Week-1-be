from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlayerSerializer

# Create your views here.

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
