from django.db import models

class Todoitem(models.Model):
        text = models.TextField(max_length = 100)
        created_date = models.DateField()
        completed_date = models.DateField()
        status = models.BooleanField(default = False)
         
        def __str__(self):
            return self.text
