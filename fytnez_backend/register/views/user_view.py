from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from fytnez_backend.register.models.user import User
from fytnez_backend.register.serializers.user_serializer import (
    UserSerializer,
    FcmTokenSerializer,
)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["put"], url_path="fcm-token")
    def update_fcm_token(self, request, pk, *args, **kwargs):
        user = get_object_or_404(User, pk=pk)
        fcm_token_serializer = FcmTokenSerializer(data=request.data)
        fcm_token_serializer.is_valid()
        # user.fcm_token = fcm_token_serializer.fcm_token
        return Response(status=status.HTTP_200_OK)
