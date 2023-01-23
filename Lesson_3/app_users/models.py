from django.db import models
from uuid import uuid4


class UserModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    class Meta:
        unique_together = ['email']