from django.db import models


# Create your models here.
class Email(models.Model):
    email = (models.EmailField(unique=True),)
    timestamp = models.DateTimeField(auto_now_add=True)


class EmailVerificationEvent(models.Model):
    parent = models.ForeignKey(Email, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)
    last_attemp_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
    expired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True
    )
