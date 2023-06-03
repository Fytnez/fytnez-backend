from django.db import models
from fytnez_backend.register.validators.user_validator import UserValidator


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    height = models.IntegerField(validators=[UserValidator.validate_not_zero])
    weight = models.IntegerField(validators=[UserValidator.validate_not_zero])
    birthday = models.DateField(validators=[UserValidator.validate_bithday])
