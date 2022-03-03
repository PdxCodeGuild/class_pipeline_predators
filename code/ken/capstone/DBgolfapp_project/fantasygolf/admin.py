from django.contrib import admin

from .models import Player

# I believe this allows the player to be seen on the admin dashboard

admin.site.register(Player)
