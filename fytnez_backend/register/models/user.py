from django.db import models

from fytnez_backend.register.models.base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    total_points = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    height = models.IntegerField(validators=[UserValidator.validate_not_zero])
    weight = models.IntegerField(validators=[UserValidator.validate_not_zero])
    birthday = models.DateField(validators=[UserValidator.validate_bithday])
