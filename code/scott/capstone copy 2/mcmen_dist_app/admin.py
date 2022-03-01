from django.contrib import admin
from . import models

admin.site.register(models.Driver)
admin.site.register(models.Property)
admin.site.register(models.Route)
admin.site.register(models.Article)