import jwt
from datetime import timezone
from django.db import models
from fytnez_backend.register.models.base_model import BaseModel
from datetime import datetime, timedelta

class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    total_points = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateField()
    token = models.CharField(max_length=64, blank=True)
    token_expiration = models.DateTimeField(null=True, blank=True)

    def generate_token(self):
        payload = {
            'user_id': self.pk,
            'is_active': self.is_active,
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
        }
        self.token = jwt.encode(payload, 'secret_key', algorithm='HS256')
        self.token_expiration = payload['exp']
        self.save()

    def is_token_valid(self):
        return (
            self.token_expiration is None
            or self.token_expiration > datetime.now(timezone.utc)
        )