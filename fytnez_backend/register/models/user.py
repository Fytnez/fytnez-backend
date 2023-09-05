import jwt
from django.contrib.auth.hashers import make_password, check_password
from datetime import timezone
from django.db import models
from fytnez_backend.register.models.base_model import BaseModel
from datetime import datetime, timedelta

class User(BaseModel):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
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
            'is_active': self.is_active or False,
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
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password or '123456')
        return super().save(*args, **kwargs)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)