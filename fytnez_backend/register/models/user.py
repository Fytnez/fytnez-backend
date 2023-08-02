from datetime import timezone
from django.db import models
from rest_framework.authtoken.models import Token
from fytnez_backend.register.models.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    total_points = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthday = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField()
    
    def delete(self,*args,**kwargs):
        self.delete_at = timezone.now()
        self.save(*args,**kwargs)

    def save(self, *args, **kwargs):    
        if not self.pk:
            super().save(*args, **kwargs)
            Token.objects.get_or_create(user=self)
        else:
            super().save(*args, **kwargs)