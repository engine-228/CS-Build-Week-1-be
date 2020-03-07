from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
from django.db import models
from undefined_world_players.models import Player




# create room class of models


class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=50, default="ROOM NAME")
    desc = models.CharField(max_length=500, default="ROOM DESCRIPTION")
    #items = models.CharField(max_length=500, default=" ")
    #map = models.IntegerField(max_length=500, default=" ")
    NORTH = models.CharField(max_length=150, default="")
    SOUTH = models.CharField(max_length=150, default="")
    EAST = models.CharField(max_length=150, default="")
    WEST = models.CharField(max_length=150, default="")
    map = models.TextField(max_length=1500, default="ROOM MAP")

    # create function to connect rooms
    def rm_connects(self, destination, heading):
        destinationID = destination.id
        reverse_dirs = {"NORTH": "SOUTH", "SOUTH": "NORTH",
                        "EAST": "WEST", "WEST": "EAST"}
        reverse_dir = reverse_dirs[heading]
        setattr(self, f"{heading}_to", destinationID)
        setattr(destination, f"{reverse_dir}_to", self)
        self.save()

    # fn to create player naming/id
    def player_handle(self, active_playerID):
        return[p.user.username for p in Player.objects.filter(rm_current=active_playerID) if p.id != int(active_playerID)]

    # fn to create player uuid
    def playerUUID(self, active_playerID):
        return[p.uuid for p in Player.objects.filter(rm_current=active_playerID) if p.id != int(active_playerID)]
