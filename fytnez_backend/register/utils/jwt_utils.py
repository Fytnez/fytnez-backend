import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings

def generate_token(user):
    
    payload = {
        'user_id': user.pk,
        'is_active': user.is_active or False,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
    }
    return jwt.encode(payload, 'secret_key', algorithm='HS256')

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, 'secret_key', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        return 'Login expirado!'
    except jwt.InvalidTokenError:
        return 'Login Invalido'