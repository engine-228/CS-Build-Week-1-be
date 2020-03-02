from django.contrib import admin
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified',)


admin.site.register(Player, PlayerAdmin)
