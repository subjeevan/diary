from django.db import models

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=40)
    status=models.CharField(max_length=40)
    