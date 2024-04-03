from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    status_toggle = models.BooleanField(default=False)
