from django.db import models
from django.contrib.auth.models import User


class ConfirmationCode(models.Model):
    confirmation_code = models.CharField(max_length=6, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
