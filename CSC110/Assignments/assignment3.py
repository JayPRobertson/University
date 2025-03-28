import doctest

GRAMS_IN_ONE_KILO = 1000

LETTER_MAX_AREA = 282
LETTER_MAX_WEIGHT = 0.05

CHARGE_STANDARD_WEIGHT = 0.03
STANDARD_CHARGE = 0.02
STANDARD_BASERATE = 1.05

CHARGE_NONSTANDARD_WEIGHT = 0.1
NONSTANDARD_CHARGE = 0.005
NONSTANDARD_BASERATE = 1.90

def get_rectangle_area(length:float, width:float) -> float: 
    '''
    returns the area of rectangle given its length and width
    Predondition: length and width >= 0
    
    >>> get_rectangle_area(2.1, 4.8)
    10.08
    >>> get_rectangle_area(5, 2.98)
    14.9
    >>> get_rectangle_area(0, 3)
    0
    >>> get_rectangle_area(7, 0)
    0
    '''
    area = length * width
    return area

def get_median(num1:float, num2:float, num3:float) -> float:
    '''
    returns the median of three given numbers
    
    >>> get_median(3.9, 2.9, 1.0)
    2.9
    >>> get_median(3.9, 2.2, 3.3)
    3.3
    >>> get_median(2.4, 9.6, 0.8)
    2.4
    >>> get_median(2.4, 9.6, 6.8)
    6.8
    >>> get_median(2.4, 3.6, 6.8)
    3.6
    >>> get_median(2.4, 0.6, 6.8)
    2.4
    >>> get_median(2.4, 2.4, 6.8)
    2.4
    >>> get_median(2.4, 10.1, 2.4)
    2.4
    >>> get_median(2.4, 0.6, 0.6)
    0.6
    '''
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return(num2)
        else:
            return(num3)
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            return(num1)
        else:
            return(num3)
    elif num3 > num2 and num3 > num1:
        if num2 > num1:
            return(num2)
        else:
            return(num1)
    else:
        if num1 == num2 or num1 == num3:
            return(num1)
        else:
            return(num2)
        
def get_average(num1:float, num2:float, num3:float) -> float:
    '''
    returns the average of three given numbers
    
    >>> get_average(3.9, 2.9, 1.0)
    2.6
    >>> get_average(0, 2, 4.4)
    2.13
    >>> get_average(0, 0, 0)
    0.0
    >>> get_average(-9.7, 9, 48.1)
    15.8
    >>> get_average(-3, -4, 2)
    -1.66
    >>> get_average(-3, -4, -1)
    -2.66
    '''
    numbers_amount = 3
    num_sum = num1 + num2 + num3
    average = num_sum/numbers_amount
    return average

def compare_median_average(num1:float, num2:float, num3:float) -> None: 
    '''
    prints the difference between the median and the average of three numbers
    
    >>> compare_median_average(10.02, 1.98, 18)
    the median is 0.02 higher than the average
    >>> compare_median_average(3.98, 1.18, 6.84)
    the median is 0.02 smaller than the average
    >>> compare_median_average(2, 1, 3)
    the median and average are approximately the same
    '''
    average = get_average(num1, num2, num3)
    median = get_median(num1, num2, num3)
    difference = median - average
    
    if difference > 0.01:
        print(f'the median is {difference:.2f} higher than the average')
    elif difference < -0.01:
        difference = average - median
        print(f'the median is {difference:.2f} smaller than the average')
    else:
        print(f'the median and average are approximately the same')
        
def is_multiple(n1:int, n2:int) -> bool:
    '''
    prints whether n1 is a multiple of n2
   
    >>> is_multiple(8, 2)
    True
    >>> is_multiple(-8, 2)
    True
    >>> is_multiple(0, 2)
    True
    >>> is_multiple(2, 0)
    False
    >>> is_multiple(9, 2)
    False
    >>> is_multiple(2, 2)
    True
    >>> is_multiple(0,0)
    True
    '''
    if n2 == 0:
        if n1 == 0:
            return True
        else:
            return False
    return not(n1 % n2 > 0)

def convert_to_multiple(n1:int, n2:int) -> int:
    '''
    returns a multiple of n2 given numbers n1 and n2
    
    >>> convert_to_multiple(8, 2)
    8
    >>> convert_to_multiple(2, 2)
    2
    >>> convert_to_multiple(2, 0)
    0
    >>> convert_to_multiple(9, 2)
    18
    '''
    num_is_multiple = is_multiple(n1, n2)
    if num_is_multiple == True:
        return n1
    else:
        product = n1 * n2
        return product

def acronym(phrase1: str, phrase2: str) -> str:
    '''
    returns the acronym of two strings
    
    >>> acronym('Get', 'Telegram')
    'GT'
    >>> acronym('hello', 'mom')
    'hm'
    >>> acronym('Placebo', 'effect')
    'Pe'
    >>> acronym('too', 'Many')
    'tM'
    >>> acronym(' ', 'Uh oh')
    ' U'
    >>> acronym('Space', ' ')
    'S '
    >>> acronym(' ', ' ')
    '  '
    >>> acronym('Testing the', 'Function')
    'TF'
    >>> acronym('123', 'ABC')
    '1A'
    '''
    acronym = phrase1[:1] + phrase2[:1]
    return acronym

def get_shipping_cost(weight:float, length:float, width:float) -> float: 
    '''
    returns the cost of shipping given the dimensions and weight of a letter
    
    Precondition: weight is in kgs and length and width is in cm
    Precondition: weight, length, and width > 0
    
    >>> get_shipping_cost(0.06, 14.1, 20) 
    1.9
    >>> get_shipping_cost(0.2, 14.5, 20) 
    2.4
    >>> get_shipping_cost(0.05, 14.5, 20) 
    1.9
    >>> get_shipping_cost(0.05, 11.28, 25) 
    1.45
    >>> get_shipping_cost(0.03, 11.28, 25) 
    1.05
    '''
    area = get_rectangle_area(length, width)
    
    #conversions from kilograms to grams
    charge_standard_grams = CHARGE_STANDARD_WEIGHT * GRAMS_IN_ONE_KILO
    charge_nonstandard_grams = CHARGE_NONSTANDARD_WEIGHT * GRAMS_IN_ONE_KILO
    weight_grams = weight * GRAMS_IN_ONE_KILO
    
    if area <= LETTER_MAX_AREA and weight <= LETTER_MAX_WEIGHT:
        if weight_grams > charge_standard_grams:
            weight_grams -= charge_standard_grams
            additional_cost = weight_grams * STANDARD_CHARGE
        else:
            additional_cost = 0
        cost = STANDARD_BASERATE + additional_cost
        return cost
    else:
        if weight_grams > charge_nonstandard_grams:
            weight_grams -= charge_nonstandard_grams
            additional_cost = weight_grams * NONSTANDARD_CHARGE
        else:
            additional_cost = 0
        cost = NONSTANDARD_BASERATE + additional_cost
        return cost