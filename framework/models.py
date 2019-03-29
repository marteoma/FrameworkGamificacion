from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    '''
    An assessment related to an specific user
    '''
    objects = models.Manager()

    name = models.CharField(null=False, max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
    wid = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)    
