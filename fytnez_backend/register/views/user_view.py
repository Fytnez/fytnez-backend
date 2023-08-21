from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fytnez_backend.register.decorators.user_decorators import token_required
from fytnez_backend.register.serializers.user_serializer import UserSerializer
from fytnez_backend.register.models.user import User

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @api_view(['POST'])
    def login(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            user.generate_token()
            return Response({'token': user.token})
        else:
            return Response({'error': 'Credenciais inválidas'}, status=400)

    @token_required
    def minha_view_protegida(request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
