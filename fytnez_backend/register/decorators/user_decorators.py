import jwt
from django.http import HttpResponseBadRequest
from fytnez_backend.register.models.user import User

def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        try:
            payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
            user_id = payload['user_id']
            user = User.objects.get(pk=user_id)
            if not user.is_token_valid():
                return HttpResponseBadRequest('Token expirado')
            request.user = user
        except (jwt.exceptions.DecodeError, User.DoesNotExist):
            return HttpResponseBadRequest('Token inválido')
        return view_func(request, *args, **kwargs)
    return wrapper