from django.db import models

from fytnez_backend.register.models.base_model import BaseModel
from fytnez_backend.register.models.achievement_type import AchievementType


class Achievement(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField()
    is_secret = models.BooleanField()
    type = models.ForeignKey(AchievementType, on_delete=models.CASCADE)    
    hex_color = models.CharField(max_length=9, default='#FFFFC107')

    def __str__(self):
        return self.name
