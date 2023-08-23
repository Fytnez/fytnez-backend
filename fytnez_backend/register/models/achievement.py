from django.db import models

from fytnez_backend.register.models.base_model import BaseModel


class Achievement(BaseModel):
    # TODO: Depois pode ser pensado com uma model a parte para configurar os parâmetros de metrica
    class Type(models.TextChoices):
        WATER_CONSUMPTION = 'WATER_CONSUMPTION', 'Water Consumption'
        WORKOUT = 'WORKOUT', 'Workout'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    points = models.IntegerField()
    is_secret = models.BooleanField()
    type = models.CharField(max_length=255, choices=Type.choices)
    icon = models.CharField(max_length=255, help_text='''
        Coloque a constante do icon do Angular de acordo com o seguinte site:
        https://api.flutter.dev/flutter/material/Icons-class.html#constants
    ''')
    hex_color = models.CharField(max_length=9, default='#FFFFC107')

    def __str__(self):
        return self.name
