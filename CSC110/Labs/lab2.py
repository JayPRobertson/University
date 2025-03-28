import doctest
import math

def print_longer(phrase1: str, phrase2: str):
    """
    prints the first phrase if phrases are the same length
    otherwise prints the longer of two phrases 
    >>> print_longer('my', 'name')
    name
    >>> print_longer('hello', 'mom')
    hello
    >>> print_longer('hello', 'world')
    hello
    """
    if len(phrase1) >= len(phrase2):
        print(phrase1)
    else:
        print(phrase2)


def print_real_roots(a: float, b: float, c: float):
    '''
    if discriminant > 0 prints the real roots of ax^2+bx+c=0 if given a, b, c 
    prints ERROR if a is 0
    otherwise prints NO REAL ROOTS
    >>> print_real_roots(2, 3, -1)
    0.281 , -1.781
    >>> print_real_roots(0, -4, 9)
    ERROR
    >>> print_real_roots(9, 2, 10)
    NO REAL ROOTS
    '''
    discriminant = b**2 - 4* a* c
    if a == 0:
        print('ERROR')
    elif discriminant < 0:
        print('NO REAL ROOTS')
    else:
        quadratic_divisor = (2* a)
        root1 = ((-b) + math.sqrt(discriminant)) / quadratic_divisor
        root2 = ((-b) - math.sqrt(discriminant)) / quadratic_divisor       
        print(f'{root1:.3f} , {root2:.3f}')
        
def print_zodiac_sign(month: str, day: int):
    '''
    print the zodiac sign for a given month and day
    >>> print_zodiac_sign('January', 20)
    Aquarius
    >>> print_zodiac_sign('February', 18)
    Aquarius
    >>> print_zodiac_sign('February', 19)
    Pisces
    >>> print_zodiac_sign('March', 20)
    Pisces
    >>> print_zodiac_sign('March', 21)
    Aries
    >>> print_zodiac_sign('April', 19)
    Aries
    >>> print_zodiac_sign('May', 20)
    Taurus
    >>> print_zodiac_sign('April', 20)
    Taurus
    >>> print_zodiac_sign('June', 20)
    Gemini
    >>> print_zodiac_sign('May', 21)
    Gemini
    >>> print_zodiac_sign('July', 22)
    Cancer
    >>> print_zodiac_sign('June', 21)
    Cancer
    >>> print_zodiac_sign('July', 23)
    Leo
    >>> print_zodiac_sign('August', 22)
    Leo
    >>> print_zodiac_sign('September', 21)
    Virgo
    >>> print_zodiac_sign('August', 23)
    Virgo
    >>> print_zodiac_sign('September', 23)
    Libra
    >>> print_zodiac_sign('October', 22)
    Libra
    >>> print_zodiac_sign('October', 23)
    Scorpio
    >>> print_zodiac_sign('November', 21)
    Scorpio
    >>> print_zodiac_sign('November', 22)
    Sagittarius
    >>> print_zodiac_sign('December', 21)
    Sagittarius
    >>> print_zodiac_sign('December', 22)
    Capricorn
    >>> print_zodiac_sign('January', 19)
    Capricorn
    '''
    if month == 'January':
        if day >=20:
            print('Aquarius')
        else:
            print('Capricorn')
    elif month == 'February':
        if day <=18:
            print('Aquarius')
        else:
            print('Pisces')
    elif month == 'March':
        if day <=20:
            print('Pisces')
        else:
            print('Aries')
    elif month == 'April':
        if day <=19:
            print('Aries')
        else:
            print('Taurus')  
    elif month == 'May':
        if day <=20:
            print('Taurus')
        else:
            print('Gemini')
    elif month == 'June':
        if day >=21:
            print('Cancer')
        else:
            print('Gemini')
    elif month == 'July':
        if day >=23:
            print('Leo')
        else:
            print('Cancer') 
    elif month == 'August':
        if day >=23:
            print('Virgo')
        else: 
            print('Leo')
    elif month == 'September':
        if day >=23:
            print('Libra')   
        else:
            print('Virgo')
    elif month == 'October':
        if day >=23:
            print('Scorpio')  
        else:
            print('Libra')
    elif month == 'November':
        if day >=22:
            print('Sagittarius')
        else:
            print('Scorpio')
    elif month == 'December':
        if day >=22:
            print('Capricorn')
        else:
            print('Sagittarius')          