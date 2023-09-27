from rest_framework import viewsets

from fytnez_backend.register.models.user_config import UserConfig
from fytnez_backend.register.serializers.user_config_serializer import UserConfigSerializer


class UserConfigView(viewsets.ModelViewSet):
    queryset = UserConfig.objects.filter(delete_at__isnull=True)
    serializer_class = UserConfigSerializer
