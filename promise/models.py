from django.db import models
from core.models import TimestampedModel
from authentication.models import User

# Create your models here.


class Promise(TimestampedModel):
    sinceWhen = models.DateTimeField()
    tilWhen = models.DateTimeField()
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
