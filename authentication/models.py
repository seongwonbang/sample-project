from django.contrib.auth.models import AbstractUser

from core.models import TimestampedModel


# Create your models here.

class User(AbstractUser, TimestampedModel):
    pass
