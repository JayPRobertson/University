import doctest

def sum_even_values(int_list:list[int]) -> int:
    '''
    returns the sum of all even values in a given list
    
    >>> sum_even_values([])
    0
    >>> sum_even_values([1,2,3,8]) 
    10
    >>> sum_even_values([-2,0,4,1])
    2
    >>> sum_even_values([1,3,5,7])
    0
    '''
    list_sum = 0
    
    for num in int_list:
        if num % 2 == 0:
            list_sum += num
    
    return list_sum

def count_above(num_list:list[float], threshold:float) -> int:
    '''
    returns number of values in a given list above a given threshold

    >>> count_above([], 5)
    0
    >>> count_above([3.001, 2.999], 3)
    1
    
    >>> lst = [1, 2, 4, 10, 11]
    >>> count_above(lst, 5.1)
    2
    >>> count_above(lst, 0)
    5
    >>> count_above(lst, 12)
    0
    >>> count_above(lst, 1)
    4
    '''
    num_above = 0
    
    for num in num_list:
        if num > threshold: 
            num_above += 1
    
    return num_above

def add1(int_list:list[int]) -> list[int]:
    '''
    given a list, returns a new list including every int in the first list + 1
    
    >>> add1([])
    []
    >>> add1([1])
    [2]
    >>> add1([2,4,1,3])
    [3, 5, 2, 4]
    >>> add1([10, 0, -10, -1])
    [11, 1, -9, 0]
    '''
    new_list = []
    
    for num in int_list:
        new_num = num + 1
        new_list.append(new_num)
        
    return new_list

def are_all_even(int_list:list[int]) -> bool: 
    '''
    returns True if all ints in a given list are even, False if otherwise
    
    >>> are_all_even([])
    True
    >>> are_all_even([1, 2, 4, 5])
    False
    >>> are_all_even([-2, 4, 6, -100])
    True
    >>> are_all_even([-2, 4, 6, 0])
    True
    '''
    is_false = 0
    
    if len(int_list) == 0:
        return True
    else:
        for num in int_list:
            if num % 2 != 0:
                is_false +=1
    
    return is_false == 0