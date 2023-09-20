from rest_framework import viewsets

from fytnez_backend.register.models.achievement import Achievement
from fytnez_backend.register.serializers.achievement_serializer import AchievementSerializer


class AchievementView(viewsets.ModelViewSet):
    queryset = Achievement.objects.filter(delete_at__isnull=True)
    serializer_class = AchievementSerializer
