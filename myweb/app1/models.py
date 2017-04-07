from django.db import models

# Create your models here.

class Employee(models.Model):
    title=models.TextField()
    text=models.TextField()
