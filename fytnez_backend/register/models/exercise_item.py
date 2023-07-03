from django.db import models
from fytnez_backend.register.models.base_model import BaseModel
from fytnez_backend.register.models.exercise import Exercise

from fytnez_backend.register.models.exercise_list import ExerciseList


class ExerciseItem(BaseModel):
    exercise_list = models.ForeignKey(ExerciseList, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    group = models.CharField(max_length=255)
    weight = models.FloatField()
    repetition = models.FloatField()
    duration = models.TimeField()
