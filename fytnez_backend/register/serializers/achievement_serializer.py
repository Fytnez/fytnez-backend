from rest_framework import serializers

from fytnez_backend.register.models.achievement import Achievement


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
        