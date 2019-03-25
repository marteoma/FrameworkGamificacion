from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    '''
    An assessment related to an specific user
    '''
    objects = models.Manager()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=100)

class Learning_Objectives(models.Model):
    '''
    Modelo correspondiente a los objetivos de aprendizaje
    '''
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    objective = models.CharField(max_length=100, null=False)
    principle = models.IntegerField(null=False, default=1)
    grade = models.IntegerField(null=False, default=1)
    evidence = models.CharField(max_length=150, null=False)
    wid = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    assesment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
