from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.TextField()