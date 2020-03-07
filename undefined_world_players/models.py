from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
from django.db import models
from undefined_world_rooms.models import Room




# create player model class


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rm_current = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="User")
    #items = models.CharField(max_length=500, default=" ")

    # create fn to initialize

    def init(self):
        if self.rm_current == 0:
            self.rm_current == Room.objects.first().id
            self.x = Room.objects.first().x
            self.y = Room.objects.first().y
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
    instance.Player.save()
