import datetime
from re import T
import django 

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

    

#Class athlete is for the disc-golfer/golfer

class Athlete(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    points = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    image = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.first_name 


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    pub_date = models.DateField()
