from rest_framework import viewsets

from fytnez_backend.register.models.user import User
from fytnez_backend.register.serializers.user_serializer import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
