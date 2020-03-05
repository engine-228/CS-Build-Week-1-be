from django.db import models
import uuid
from undefined_world_players.player_models import Player

# create room class of models


class Room(models.Model):
    from .player_models import Player
    name = models.CharField(max_length=50, default="ROOM NAME")
    desc = models.CharField(max_length=500, default="ROOM DESCRIPTION")
    #items = models.CharField(max_length=500, default=" ")
    #map = models.IntegerField(max_length=500, default=" ")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    # add x,y to locate rooms in the grid
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    # create function to connect rooms
    def rm_connects(self, destination, heading):
        destinationID = destination.id
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[heading]
        setattr(self, f"{heading}_to", destinationID)
        setattr(destination, f"{reverse_dir}_to", self.id)
        self.save()

    # fn to create player naming/id
    def player_handle(self, active_playerID):
        return[p.user.username for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]

    # fn to create player uuid
    def playerUUID(self, active_playerID):
        return[p.uuid for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]
