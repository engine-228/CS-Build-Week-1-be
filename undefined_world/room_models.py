from django.db import models 
import uuid
from .player_models import Player


# create room class of models

class Room(models.Model):
    title = models.CharField(max_length=50, default="TITLE")
    description = models.CharField(max_length=500, default="DESCRIPTION")
    items = models.CharField(max_length=500, default=" ")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)

    # create function to connect rooms
    def rm_connects(self, destination, heading):
        destinationID = destination.id 
        try:
            destination = Room.objects.get(id=destinationID)
        except Room.DoesNotExist:
            print("Room doesn't exist") 
        else:
            if heading == 'n':
                self.n_to = destinationID
            elif heading =='s':
                self.s_to = destinationID
            elif heading == 'e':
                self.e_to = destinationID
            elif heading =='w':
                self.w_to = destinationID
            else:
                print("You can't go that way.")
                return
            self.save()

    # fn to create player naming/id
    def player_handle(self, active_playerID):
        return[p.user.username for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]

    # fn to create player uuid
    def playerUUID(self, active_playerID):
        return[p.uuid for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]
                                     


