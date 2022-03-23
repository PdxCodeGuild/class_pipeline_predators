from django.db import models

class Keywordsearch(models.Model):
    searchbar = models.TextField(30)
    def __str__(self):
        return self.searchbar

class Motorcycles(models.Model):
    make = models.TextField(max_length=15)
    modelname = models.TextField(max_length=15)
    year = models.TextField(max_length=5)
    def __str__(self):
        return self.modelname


    
