from django.db import models
from django.db.models.fields import NullBooleanField

class Product(models.Model):
  title = models.CharField(max_length=200)
  image = models.CharField(max_length=200)
  likes = models.PositiveIntegerField(default=0)

class User(models.Model):
  name = models.CharField(max_length=200, null=True)
