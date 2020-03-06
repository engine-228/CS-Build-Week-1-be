from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WorldSerializer
from .models import World

# Create your views here.

class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer
