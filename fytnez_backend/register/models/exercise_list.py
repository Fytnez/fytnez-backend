from django.db import models
from fytnez_backend.register.models.base_model import BaseModel

from fytnez_backend.register.models.user import User


class ExerciseList(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_public = models.IntegerField()