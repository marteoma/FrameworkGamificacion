from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     identifier = models.CharField(max_length=20, unique=True)
#     USERNAME_FIELD = 'identifier'

class Learning_Objectives(models.Model):
    id = models.AutoField(primary_key=True)
    objective = models.CharField(max_length=300, null=False)