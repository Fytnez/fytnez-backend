from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self,*args,**kwargs):
        self.update_at = timezone.now()
        return super().save(*args,**kwargs)
    
    def delete(self,*args,**kwargs):
        self.delete_at = timezone.now()
        self.save(*args,**kwargs)
