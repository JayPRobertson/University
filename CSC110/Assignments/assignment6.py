import doctest

def multiply_by(num_list:list, multiplier:int) -> list[float]:
    '''
    creates and returns a new list containing every variable in a given 
    list multiplied by a given multiplier
    
    Precondition: all values in a given list can mulptiplied by an int
    
    >>> multiply_by([], 3)
    []
    >>> multiply_by([1, 2, 3, 4], 2)
    [2, 4, 6, 8]
    >>> multiply_by([1.7, -2, 3, -4], -3)
    [-5.1, 6, -9, 12]
    >>> multiply_by([0,-2, 13, 1.6], 4)
    [0, -8, 52, 6.4]
    
    >>> multiply_by(['splat', 'ratchet', 'BCAT', 'at', 'atlast'], 2)
    ['splatsplat', 'ratchetratchet', 'BCATBCAT', 'atat', 'atlastatlast']
    >>> multiply_by(['splat', 'ratchet', 'BCAT', 'at', 'atlast'], -5)
    ['', '', '', '', '']
    
    >>> multiply_by([True, False], 5)
    [5, 0]
    >>> multiply_by([True, False], -1)
    [-1, 0]
    '''
    new_list = []
    
    for num in num_list:
        new_num = num * multiplier
        new_list.append(new_num)
    
    return new_list

def get_below(int_list:list[int], threshold:int) -> list[float]:
    '''
    returns a new list containing every variable in a given list which is
    less than a given threshold
    
    >>> get_below([], 4)
    []
    
    >>> lst = [-4, -1, 0, 1, 5, 10]
    >>> get_below(lst, 0)
    [-4, -1]
    >>> get_below(lst, -4)
    []
    >>> get_below(lst, 11)
    [-4, -1, 0, 1, 5, 10]
    '''
    new_list = []
    
    for num in int_list:
        if num < threshold:
            new_list.append(num)
    
    return new_list

def remove_negatives(int_list:list[int]) -> list[int]:
    '''
    returns a new list containing every variable in a given list which is 
    positive 
    
    >>> remove_negatives([])
    []
    >>> remove_negatives([0, -1, 2, 3])
    [0, 2, 3]
    >>> remove_negatives([-4, -2, -3, -1])
    []
    >>> remove_negatives([1, 2, 3, 4])
    [1, 2, 3, 4]
    '''
    new_list = []
    
    for num in int_list:
        if num >= 0:
            new_list.append(num)
            
    return new_list

def contains_above(num_list:list[float], threshold:float) -> bool:
    '''
    returns whether num_list contains a value >= a given threshold
    
    >>> contains_above([], 0)
    False
    
    >>> lst = [-4, -1, 0, 1, 5, 10]
    >>> contains_above(lst, -4)
    True
    >>> contains_above(lst, 11)
    False
    >>> contains_above(lst, 10)
    False
    '''
    is_true = 0
    
    for num in num_list:
        if num > threshold:
            is_true += 1
    
    return is_true > 0

def get_smallest(num_list:list[float]) -> None:
    '''
    returns the smallest value in a given list
    
    Precondition: num_list must have at least one variable
    
    >>> get_smallest([1])
    1
    >>> get_smallest([-2, 3])
    -2
    >>> get_smallest([0.0001, 0.001, 0.0002, 0.01])
    0.0001
    >>> get_smallest([0, 1, 2, 3])
    0
    '''
    prev = num_list[0]
    
    for index in range(len(num_list)):
        if prev > num_list[index]:
            prev = num_list[index]
    
    return prev     

def count_ends_with(str_list:list[str], string:str) -> int:
    '''
    returns the number of strings in a given string list that end in a 
    given string (ignores case)
    
    >>> count_ends_with([], 'ses')
    0
    >>> count_ends_with(['abCD', 'efg', 'ABC', 'cd', 'c', 'dcgcd'], 'CD')
    3
    
    >>> lst = ['splat', 'ratchet', 'BCAT', 'at', 'atlast']
    >>> count_ends_with(lst, 'at')
    3
    >>> count_ends_with(lst, 'LAT')
    1
    '''
    string = string.lower()
    str_length = len(string)
    is_true = 0
    
    for str_val in str_list:
        str_val = str_val.lower()
        val_length = len(str_val)
        start_val = (val_length - str_length)
        if string in str_val[start_val:]: 
            is_true +=1
            
    return is_true