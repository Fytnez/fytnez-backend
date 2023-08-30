from django.db import models

from fytnez_backend.register.models.base_model import BaseModel
from fytnez_backend.register.models.user import User
from fytnez_backend.register.models.achievement import Achievement

class UserAchievement(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achieved_on = models.DateTimeField(auto_now_add=True)
    