from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_date = models.DateField()
    completed_date = models.DateField()

    def __str__(self):
        return self.title
