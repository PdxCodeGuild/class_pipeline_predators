from django.contrib import admin

from .models import Article, Athlete

# I believe this allows the player to be seen on the admin dashboard

admin.site.register(Athlete)
admin.site.register(Article)