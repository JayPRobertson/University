import doctest

WARN_ALCOHOL_MIN = 50
FAIL_ALCOHOL_MIN = 80

FAILURE_FINE = 1430
THIRD_WARN_FINE = 1330
SECOND_WARN_FINE = 780
FIRST_WARN_FINE = 600

FAIL_DP_LENGTH = 90 
FAIL_VI_LENGTH = 30
THIRD_WARN_DP_LENGTH = 30
SECOND_WARN_DP_LENGTH = 7
FIRST_WARN_DP_LENGTH = 3
THIRD_WARN_VI_LENGTH = 30
SECOND_WARN_VI_LENGTH = 7
FIRST_WARN_VI_LENGTH = 3

def print_qualification_status(trial_time: float, qualification_time:float):
    '''
    determines whether a racer qualified for an Olympic event
    prints the amount of time a racer qualified below qualifying time
    otherwise prints the amount of time over the qualifying time
    
    Precondition: trial_time and qualification_time must be in seconds
    
    >>> print_qualification_status (30.22, 39.71)
    You qualified at 9.49 seconds below qualifying time
    >>> print_qualification_status (51.23, 39.71)
    You missed qualifying by 11.52 seconds
    '''
    if trial_time <= qualification_time:
        under_qualifying_time = qualification_time - trial_time
        print(f'You qualified at {under_qualifying_time:.2f} seconds below qualifying time')
    else:
        over_qualifying_time = trial_time - qualification_time
        print(f'You missed qualifying by {over_qualifying_time:.2f} seconds')

def print_median(num1: float, num2: float, num3: float):
    '''
    prints the median of three given numbers
    
    >>> print_median(3.9, 2.9, 1.0)
    2.9
    >>> print_median(3.9, 2.2, 3.3)
    3.3
    >>> print_median(2.4, 9.6, 0.8)
    2.4
    >>> print_median(2.4, 9.6, 6.8)
    6.8
    >>> print_median(2.4, 3.6, 6.8)
    3.6
    >>> print_median(2.4, 0.6, 6.8)
    2.4
    >>> print_median(2.4, 2.4, 6.8)
    2.4
    >>> print_median(2.4, 10.1, 2.4)
    2.4
    >>> print_median(2.4, 0.6, 0.6)
    0.6
    '''
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(num2)
        else:
            print(num3)
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    elif num3 > num2 and num3 > num1:
        if num2 > num1:
            print(num2)
        else:
            print(num1)
    else:
        if num1 == num2 or num1 == num3:
            print(num1)
        else:
            print(num2) 

def print_triangle_type(a: float, b: float, c: float):
    '''
    prints the type of a triangle given its dimensions
    
    >>> print_triangle_type(3, 4, 5)
    scalene
    >>> print_triangle_type(3, 3, 5)
    isosceles
    >>> print_triangle_type(3, 4, 4)
    isosceles
    >>> print_triangle_type(3, 2, 3)
    isosceles
    >>> print_triangle_type(3, 3, 3)
    equilateral
    '''
    if a == b and a == c:
        print('equilateral')
    elif a == b or b == c or a == c:
        print('isosceles')
    else:
        print('scalene')

def is_multiple_of(n1: int, n2: int):
    '''
    prints whether n1 is a multiple of n2
   
    >>> is_multiple_of(8, 2)
    8 is a multiple of 2
    >>> is_multiple_of(-8, 2)
    -8 is a multiple of 2
    >>> is_multiple_of(0, 2)
    0 is a multiple of 2
    >>> is_multiple_of(2, 0)
    2 is not a multiple of 0
    >>> is_multiple_of(9, 2)
    9 is not a multiple of 2
    >>> is_multiple_of(2, 2)
    2 is a multiple of 2
    '''
    if n2 == 0 or n1 % n2 > 0:
        print(n1, 'is not a multiple of', n2)
    else:
        print(n1, 'is a multiple of', n2)
        
def print_roadside_penalty(blood_alcohol: int, incident_num: int, did_breath_sample: bool):
    '''
    prints the penalties of a breathalyzer test based on given blood alcohol 
    level, incident number, and whether the test was completed
    
    Precondition: blood_alcohol >= 0 and is in alcohol mg/100mL of blood
    Precondition: incident_num >= 1
    
    >>> print_roadside_penalty(60, 3, False)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    >>> print_roadside_penalty(90, 2, True)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    >>> print_roadside_penalty(60, 3, 3>5)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    >>> print_roadside_penalty(90, 2, 5>3)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    
    >>> print_roadside_penalty(10, 2, True)
    no penalty
    >>> print_roadside_penalty(10, 2, 5>3)
    no penalty
    
    >>> print_roadside_penalty(74, 1, True)
    Driving Prohibition Length: 3 days
    Vehicle Impoundment Length: 3 days
    Penalties and fees: $600
    >>> print_roadside_penalty(69, 2, True)
    Driving Prohibition Length: 7 days
    Vehicle Impoundment Length: 7 days
    Penalties and fees: $780
    >>> print_roadside_penalty(77, 3, True)
    Driving Prohibition Length: 30 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1330
    
    >>> print_roadside_penalty(74, 1, 5>3)
    Driving Prohibition Length: 3 days
    Vehicle Impoundment Length: 3 days
    Penalties and fees: $600
    >>> print_roadside_penalty(69, 2, 5>3)
    Driving Prohibition Length: 7 days
    Vehicle Impoundment Length: 7 days
    Penalties and fees: $780
    >>> print_roadside_penalty(77, 3, 5>3)
    Driving Prohibition Length: 30 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1330
    '''  
    if did_breath_sample == False or blood_alcohol >= FAIL_ALCOHOL_MIN:
        print(f'Driving Prohibition Length: {FAIL_DP_LENGTH} days')
        print(f'Vehicle Impoundment Length: {FAIL_VI_LENGTH} days')
        print(f'Penalties and fees: ${FAILURE_FINE}')
    elif blood_alcohol < WARN_ALCOHOL_MIN:
        print('no penalty')
    else:
        if incident_num == 1:
            print(f'Driving Prohibition Length: {FIRST_WARN_DP_LENGTH} days')
            print(f'Vehicle Impoundment Length: {FIRST_WARN_VI_LENGTH} days')
            print(f'Penalties and fees: ${FIRST_WARN_FINE}')            
        elif incident_num == 2:
            print(f'Driving Prohibition Length: {SECOND_WARN_DP_LENGTH} days')
            print(f'Vehicle Impoundment Length: {SECOND_WARN_VI_LENGTH} days')
            print(f'Penalties and fees: ${SECOND_WARN_FINE}')              
        else:
            print(f'Driving Prohibition Length: {THIRD_WARN_DP_LENGTH} days')
            print(f'Vehicle Impoundment Length: {THIRD_WARN_VI_LENGTH} days')
            print(f'Penalties and fees: ${THIRD_WARN_FINE}')              