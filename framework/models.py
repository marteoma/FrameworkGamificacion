from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    '''
    An assessment related to an specific user
    '''
    objects = models.Manager()

    name = models.CharField(null=False, max_length=100)
    level = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "owner")


class Evidence(models.Model):
    '''
    Represents all the evidence of a principle on an strategy
    '''
    objects = models.Manager()

    sort = models.IntegerField(null=False, default=1)
    description = models.CharField(null=False, max_length=500)

    def __str__(self):
        return self.description

class Principle(models.Model):
    '''
    Modelo correspondiente a los principios 
    '''
    objects = models.Manager()
        
    principle = models.IntegerField(null=False, default=1, primary_key=True)
    grade = models.IntegerField(null=False, default=1)
    justification = models.CharField(max_length=150, null=False)
    wid = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    evidence = models.ForeignKey(Evidence, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("assessment", "principle")
