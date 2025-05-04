from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Email(models.Model):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    


class EmailVerificationEvent(models.Model):
    parent = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid1)
    timestamp = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)
    last_attemp_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    expired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    
    def get_link(self):
        return f"{settings.BASE_URL}/verify/{self.token}/"
    
