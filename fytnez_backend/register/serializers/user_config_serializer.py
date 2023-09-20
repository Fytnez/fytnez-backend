from rest_framework import serializers

from fytnez_backend.register.models.user_config import UserConfig


class UserConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserConfig
        fields = '__all__'