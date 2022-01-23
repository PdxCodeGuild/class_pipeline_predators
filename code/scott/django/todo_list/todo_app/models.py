from django.db import models

class Todo(models.Model):
    todo_item = models.CharField(max_length = 20)
    text = models.TextField(max_length = 500)
    create_date = models.DateField()
    finish_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_item
        
