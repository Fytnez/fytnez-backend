from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fytnez_backend.register.serializers.user_serializer import UserSerializer
from fytnez_backend.register.models.user import User
from fytnez_backend.register.utils.jwt_utils import generate_token, decode_jwt_token

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @api_view(['POST'])
    def login(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None or not user.check_password(password):
             return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token = generate_token(user)
        return Response({'token': token})
    
    @api_view(['POST'])
    def validate_token(request):
        token = request.data.get('token')

        if not token:
            return Response({'error': 'Token não fornecido'}, status=status.HTTP_400_BAD_REQUEST)

        payload = decode_jwt_token(token)

        if payload is None:
            # O token é inválido
            return Response({'valid': False, 'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # O token é válido
            return Response({'valid': True}, status=status.HTTP_200_OK)
