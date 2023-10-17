from rest_framework import viewsets
from fytnez_backend.register.models.exercise import Exercise

from fytnez_backend.register.serializers.exercise_serializer import ExerciseSerializer


class ExerciseView(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
