from django.db import models
from uuid import uuid4


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=150)
