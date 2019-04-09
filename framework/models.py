from django.db import models
from django.contrib.auth.models import User
from .choices import GRADE_CHOICES, PRINCIPLE_CHOICES

'''
Constants
'''
#Roles
r = 10
#Materials
m = 5
#Steps
s = 5

class Assessment(models.Model):
    '''
    An assessment related to an specific user
    '''
    #TODO: This model has to be fixed to create an user independente counter
    objects = models.Manager()

    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def level(self):
        #List of Wid for all the principles of the strategy
        lw =  list(Principle.objects.filter(assessment_id=self.id))
        acum = 0
        for i in lw:
            acum += i.W()
        return round(acum / len(lw), 2)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "owner")


class Principle(models.Model):
    '''
    Modelo correspondiente a los principios 
    '''
    objects = models.Manager()
        
    principle = models.IntegerField(null=False, default=1)
    grade = models.IntegerField(null=False, default=1)
    justification = models.CharField(max_length=150, null=False)

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)

    def W(self):
        ''' Get the weight of this principle in the assessment '''
        return (self.Tlg() + self.Tru() + r + m + s) * self.grade

    def Tlg(self):
        ''' Get the real total of goals '''
        return (self.count(self.principle) * 40) / self.count()

    def Tru(self):
        ''' Get the real total of rules '''
        return (self.count(self.principle) * 30) / self.count()

    def count(self, p: int = 0):
        '''Count the amount of learning objectives for the specified principle.
        If no principle is passed will count all the objectives.

        Parameters
        ----------
        p : int
            Id of the principle
            If none, all the principles will count
        
        Returns
        -------
        int
            Amount of learning objectives
        '''
        if p == 0:
            return Principle.objects.filter(assessment_id=self.assessment).count()
        else:
            return Principle.objects.filter(principle=p, assessment_id=self.assessment).count()

    def showGrade(self):
        ''' Conver the grade into its text equivalent '''
        return dict(GRADE_CHOICES)[self.grade]
    
    def showPrinciple(self):
        ''' Conver the principle identifier into its text equivalent '''
        return dict(PRINCIPLE_CHOICES)[self.principle]

    class Meta:
        unique_together = ("assessment", "principle")

class Evidence(models.Model):
    '''
    Represents all the evidence of a principle on an strategy
    '''
    objects = models.Manager()

    sort = models.IntegerField(null=False, default=1)
    description = models.CharField(null=False, max_length=500)

    principle = models.ForeignKey(Principle, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
