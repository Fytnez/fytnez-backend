from django.db import models

from fytnez_backend.register.models.base_model import BaseModel


class Exercise(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)