from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateField()
