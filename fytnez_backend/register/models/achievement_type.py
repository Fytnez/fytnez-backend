from django.db import models

from fytnez_backend.register.models.base_model import BaseModel

class AchievementType(BaseModel):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, help_text='''
        Coloque a constante do icon do Angular de acordo com o seguinte site:
        https://api.flutter.dev/flutter/material/Icons-class.html#constants
    ''')