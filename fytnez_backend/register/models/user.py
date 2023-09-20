from django.db import models

from fytnez_backend.register.models.base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    total_points = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateField()
    fcm_token = models.CharField(blank=True, null=True, max_length=255)
