from rest_framework import serializers

from fytnez_backend.register.models.exercise import Exercise



class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ["name", "description", "create_at", "update_at", "delete_at"]
