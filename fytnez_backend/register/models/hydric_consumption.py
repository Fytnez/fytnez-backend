from fytnez_backend.register.models.base_model import BaseModel
from django.db import models

from fytnez_backend.register.models.user import User

class HydricConsumption(BaseModel):
    qnty_consumption = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()