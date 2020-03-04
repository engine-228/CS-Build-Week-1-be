from django.contrib.auth.models import User
from undefinedapi.models import Room, Player 

from undefinedapi.models import Player, rooms


Room.objects.all().delete()

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")

rm_outside = Room(title=" ", description=" ", items=" ")


r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()
r_outside.save()

# hook up the rooms
r_outside.connect(r_tbd, "n")
r_outside.connect(r_tbd, "s")
r_outside.connect(r_tbd, "e")
r_outside.connect(r_tbd, "w")
r_outside.connect(r_tbd, "n")
r_outside.connect(r_tbd, "w")
r_outside.connect(r_tbd, "w")
r_outside.connect(r_tbd, "e")
r_outside.connect(r_tbd, "s")
r_outside.connect(r_tbd, "w")
r_outside.connect(r_tbd, "e")

players = Player.objects.all()
for p in players:
    p.rm_current = r_outside.id 
    p.save()

