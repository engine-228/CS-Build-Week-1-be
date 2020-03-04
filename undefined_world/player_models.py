from django.db import models  
from .room_models import Room 
from django.dispatch import receiver 
import uuid
import sys

# create player model class
class Player(models.Model):
    user = models.models.OneToOneField(User, on_delete=models.CASCADE)
    rm_current = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    items = models.CharField(max_length=500, default=" ")


    # create fn to initialize
    def init(self):
        if self.rm_current == 0:
            self.rm_current == Room.objects.first().id
            self.save()

    def room(self):
        try:
            return Room.objects.get(id=self.rm_current)  
        except Room.DoesNotExist:
            self.init()
            return self.room()

@receiver(post_save, sender=User)

# fn to create player
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)

def save_player(sender, instance, **kwargs):
    instance.player.save()

