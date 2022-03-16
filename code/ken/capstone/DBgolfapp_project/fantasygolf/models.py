import datetime 

from django.db import models
from django.utils import timezone

#Class player is basically for the user

class Player(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
 
 #Class event is for the events the athletes play in 

class Event(models.Model):
    name = models.CharField(max_length=200)



#Class athlete is for the disc-golfer/golfer

class Athlete(models.Model):
    name = models.CharField(max_length=200)
    events_played_in = models.ForeignKey( Event , on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name 


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    pub_date = models.DateField()
