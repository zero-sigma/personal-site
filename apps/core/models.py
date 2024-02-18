from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)