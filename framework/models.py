from django.db import models
from django.contrib.auth.models import AbstractUser
from framework.choices import *

# Create your models here.
# class User(AbstractUser):
#     identifier = models.CharField(max_length=20, unique=True)
#     USERNAME_FIELD = 'identifier'

#Modelo correspondiente a los objetivos de aprendizaje
class Learning_Objectives(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    objective = models.CharField(max_length=100, null=False)
    principle = models.IntegerField(null=False, default=1)
    grade = models.IntegerField(null=False, default=1)
    evidence = models.CharField(max_length=150, null=False)
    wid = models.IntegerField(null=False, default=1)