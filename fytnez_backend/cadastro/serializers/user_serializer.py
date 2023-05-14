from rest_framework import serializers

from fytnez_backend.cadastro.models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password", "height", "weight", "birthday"]
