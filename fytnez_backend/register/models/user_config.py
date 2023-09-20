from django.db import models

from fytnez_backend.register.models.base_model import BaseModel
from fytnez_backend.register.models.user import User


class UserConfig(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dailyHydricComsumption = models.IntegerField(help_text="ml")