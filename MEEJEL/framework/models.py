from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    identifier = models.CharField(max_length=20, unique=True)
    USERNAME_FIELD = 'identifier'