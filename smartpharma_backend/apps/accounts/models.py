Sure, here's the contents for the file `/smartpharma_backend/smartpharma_backend/apps/accounts/models.py`:

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email