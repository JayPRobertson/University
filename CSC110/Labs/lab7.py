import doctest

#represents the information of a flight 
#tuple[departure city, arrival city, duration of the flight]
#duration > 0 and is in hours, city names != [] and have proper capitalization
FlightInfo = tuple[str, str, float]

DEPART_CITY = 0
ARRIVE_CITY = 1
DURATION = 2


def swap(lst:list, pos1:int, pos2:int) -> None:
    '''
    updates a given list with values in positions given by pos1 and 
    pos2 swapped
    
    Precondition: pos1 and pos2 are valid positions in lst
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 0, 1)
    >>> lst
    ['rat', 'cat', 0.4, -2, 1.9, 3, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 2, 4)
    >>> lst
    ['cat', 'rat', 1.9, -2, 0.4, 3, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 3, 5)
    >>> lst
    ['cat', 'rat', 0.4, 3, 1.9, -2, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 3, 7)
    >>> lst
    ['cat', 'rat', 0.4, False, 1.9, 3, True, -2]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 0, 7)
    >>> lst
    [False, 'rat', 0.4, -2, 1.9, 3, True, 'cat']
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 0, 2)
    >>> lst
    [0.4, 'rat', 'cat', -2, 1.9, 3, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 0, 3)
    >>> lst
    [-2, 'rat', 0.4, 'cat', 1.9, 3, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 2, 3)
    >>> lst
    ['cat', 'rat', -2, 0.4, 1.9, 3, True, False]
    
    >>> lst = ['cat', 'rat', 0.4, -2, 1.9, 3, True, False]
    >>> swap(lst, 2, 7)
    >>> lst
    ['cat', 'rat', False, -2, 1.9, 3, True, 0.4]
    '''
    num1 = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = num1

def index_of_smallest(lst:list) -> int:
    '''
    returns the position of the smallest value in a given list
    if string is empty, returns -1
    
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    >>> index_of_smallest([True, False])
    1
    >>> index_of_smallest([True, False, 3, 1.1, -5, -5])
    4
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest( ['a', 'b', 'd', 'c', 'A'])
    4
    ''' 
    position = 0
    
    if lst == []:
        return -1
    else:
        smallest = lst[0]
        index = 1         
        while index < len(lst):
            if smallest > lst[index]:
                position = index
                smallest = lst[index]
            index += 1
    
    return position

def total_duration(info:list[FlightInfo]) -> float:
    '''
    returns the total duration of all flights in info
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), \
    ('Vancouver', 'Toronto', 4)])
    9.5
    >>> total_duration([('Victoria', 'Tokyo', 10.5), \
    ('Vancouver', 'Seattle', 5), ('Vancouver', 'Toronto', 4)])
    19.5
    >>> total_duration([('Victoria', 'Vancouver', 0.5), \
    ('Vancouver', 'Calgary', 1)])
    1.5
    '''
    total_duration = 0
    for flight in info:
        total_duration += flight[DURATION]
    
    return total_duration

def get_destinations_from(info:list[FlightInfo], depart:str) -> list[str]:
    '''
    returns a list of all unique destinations from info flown to from a given 
    departure city (depart)
    
    Precondition: depart has proper capitalization
    
    >>> lst = [('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), \
    ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)]
    >>> get_destinations_from(lst, 'Victoria')
    ['Vancouver', 'Calgary']
    >>> get_destinations_from(lst, 'Vancouver')
    ['Toronto']
    >>> get_destinations_from(lst, 'Kelowna')
    []
    >>> get_destinations_from(lst, '')
    []
    >>> get_destinations_from(lst, 'VancouvorVancouver')
    []
    '''
    city_list = []
    for flight in info:
        flight_depart = flight[DEPART_CITY]
        flight_arrive = flight[ARRIVE_CITY]
        if depart == flight_depart and not flight_arrive in city_list:
            city_list.append(flight_arrive)
            
    return city_list