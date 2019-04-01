'''
This file contains functions that might help the procedures.
'''
from framework.models import Assessment, Learning_Objectives
from django.db.models import Avg

'''
Constants
'''
#Roles
r = 10
#Materials
m = 5
#Steps
s = 5

def calc_level(assessment: int):
    ''' Calculates the level of gamification of the assessment
    '''
    try:
        acum = 0
        for i in range(1,11,1):
            acum += __W(i, assessment)
        acum = round(acum,2)
        return __LW(acum)
    except:
        return 'Un error ha ocurrido durante el cálculo, revise que tenga principios'

def __Tlg(principle: int, assessment):
    ''' Gets the number of learning goals identified in the game elements
    
    Parameters
    ----------
    principle : int
        The principle to calculate the total of rules
    
    Returns
    -------
    float
        Total learning goals for the principle
    '''
    return (__CountPrinciple(p=principle, a=assessment) * 40) / __CountPrinciple(a=assessment)

def __Tru(principle: int, assessment):
    ''' this is useless
    '''
    return (__CountPrinciple(p=principle, a=assessment) * 30) / __CountPrinciple(a=assessment)

def __W(principle: int, assessment):
    ''' Gets weight of each principle

    Parameters
    ----------
    principle : int
        Id of the principle

    Returns
    -------
    float
        Principle Weight
    '''
    Tlg = __Tlg(principle, assessment)
    Tru = __Tru(principle, assessment)
    Gr = Learning_Objectives.objects.filter(principle=principle, assessment_id=assessment)\
        .aggregate(Avg('grade'))['grade__avg']
    W = 0
    if Gr != None:
        W = (Tlg + Tru + r + m + s) * Gr
    
    return W

def __LW(W: float):
    ''' Percentaje of incorporation of gamification in the enviroment

    Parameters
    ----------
    W : float
        Principle Weight

    Returns
    -------
    float
        Gamification level
    '''
    return W / 50


def __CountPrinciple(p: int = 0, a: int = 1):
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
        return Learning_Objectives.objects.filter(assessment_id=a).count()
    else:
        return Learning_Objectives.objects.filter(principle=p, assessment_id=a).count()
    