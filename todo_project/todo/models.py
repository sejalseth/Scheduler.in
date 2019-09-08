from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    date = models.DateField()
    time = models.TimeField()