'''
This file contains functions that might help the procedures.
'''

def calc_level(r: int, m: int, s: int, Gr: int) -> float:
    '''Right now this method does not too much
    '''
    Tlg = 40
    Tru = 30
    W = __W(Tlg, Tru,Gr, r, m, s)
    return __LW(W)

def __Tlg(n: int, x: int):
    ''' Gets the number of learning goals identified in the game elements
    
    Parameters
    ----------
    n : int
        Quantity of learning goals
    x : int
        Quantity of learning goals for each principle

    Returns
    -------
    float
        Total learning goals
    '''
    return (40 * x) / n

def __Tru(m: int, y: int):
    ''' Gets the number of game rules in the game elements

    Parameters
    ----------
    m : int
        Quantity of rules
    y : int
        Quantity of rules for each principle

    Returns
    -------
    float
        Total rules
    '''
    return  (30 * y) / m

def __W(Tlg: float, Tru: float, Gr: int, r: int, m: int, s: int):
    ''' Gets weight of each principle

    Parameters
    ----------
    Tlg : float
        Total learning goals
    Tru : float
        Total rules
    Gr : int
        Grade
    r : int
        Roles
    m : int
        Materials
    s : int
        Steps

    Returns
    -------
    float
        Principle Weight
    '''
    return (Tlg + r + m + s) * Gr


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
