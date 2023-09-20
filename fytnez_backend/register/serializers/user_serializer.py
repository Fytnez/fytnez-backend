from rest_framework import serializers
from rest_framework.serializers import ValidationError

from fytnez_backend.register.models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "height",
            "weight",
            "birthday",
            "fcm_token",
        ]


class FcmTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["fcm_token"]

    def validate_fcm_token(self, value: str):
        if value is None or value == "":
            raise ValidationError("Required field")
        return value
