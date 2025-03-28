import doctest

SPACE = ' '

BASE_SMALLEST_ROOF = 11
BASE_SMALLEST_FLOOR = 5

SMALLEST_FACE = 13

SMALLEST_TOP = 7
TOP_INITIAL_SPACE = 3


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

def get_factors(n:int) -> str:
    '''
    returns a string of all factors of n
    Precondition: n > 0
    
    >>> get_factors(1)
    '1'
    >>> get_factors(12)
    '1,2,3,4,6,12'
    >>> get_factors(30)
    '1,2,3,5,6,10,15,30'
    '''
    num = 2
    factors_list = ''
    
    for factors in range(2, n+1):
        if is_multiple(n, num) == True:
            num_string = str(num)
            factors_list = factors_list + ',' + num_string
        num +=1
        
    return '1' + factors_list
        

def sum_fibonacci_sequence(n:int) -> int:
    '''
    returns the sum of the first n values in the fibonacci sequence
    Precondition: n >= 0
    
    >>> sum_fibonacci_sequence(7)
    20
    >>> sum_fibonacci_sequence(3)
    2
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(0)
    0
    '''
    previous_num = 0
    current_num = 1
    
    if n == 0:
        return 0
    else:
        for sum_sequence in range(n):    
            next_num = previous_num + current_num
            previous_num = current_num
            current_num = next_num
        return(next_num - 1)

def factorial(num:int) -> int:
    '''
    returns the factorial of a given number
    Precondition: num >= 0
    
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    >>> factorial(6)
    720
    '''
    n = num
    quotient = 1
    
    for count in range(n, 0, -1):
        quotient = quotient * n
        n = n-1
    
    return quotient

def draw_base(size:int, num_floors:int) -> None:
    '''
    prints the base of a clock given the size of the tower and the number 
    of floors
    
    Precondition: size and num_floors >=0
    '''
    roof_scale = BASE_SMALLEST_ROOF + 2* size
    floor_scale = BASE_SMALLEST_FLOOR + size
    
    for draw in range(1, num_floors+1):
        print(2*SPACE, roof_scale* '_', sep = '')
        print(1*SPACE, '|', roof_scale* '_', '|', sep = '')
        for scale in range(1, size+BASE_SMALLEST_FLOOR):
            print (2*SPACE, floor_scale*'|', SPACE, floor_scale*'|', sep = '') 

def draw_face(size:int) -> None:
    '''
    prints the face of a clock given the size of the tower
    Precondition: size and base_lvls >=0
    '''
    clock_size = SMALLEST_FACE + 2*size
    
    outline = '-' * clock_size
    clock_inside = '~' * clock_size
    face_edge = '~' * size
    
    print('|', outline, '|', sep ='')
    for draw in range(size):
        print('|', clock_inside, '|', sep ='')
    print('|', face_edge, '|-----------|', face_edge, '|', sep = '')
    print('|', face_edge, '|@  **^**  @|', face_edge, '|', sep = '')
    print('|', face_edge, '|  ** | **  |', face_edge, '|', sep = '')
    print('|', face_edge, '| *   @-->* |', face_edge, '|', sep = '')
    print('|', face_edge, '|  **   **  |', face_edge, '|', sep = '')
    print('|', face_edge, '|@  *****  @|', face_edge, '|', sep = '')
    print('|', face_edge, '|-----------|', face_edge, '|', sep = '')
    for draw in range(size):
        print('|', clock_inside, '|', sep ='')      
    print('|', outline, '|', sep ='')  

def draw_top(size:int) -> None:
    '''
    prints the top of a clock given the size of the tower
    Precondition: size and base_lvls >=0
    '''
    top_size = SMALLEST_TOP + 2 * size
    start_space = size + TOP_INITIAL_SPACE 
    
    print(TOP_INITIAL_SPACE* SPACE, '|', top_size*'*', '|', sep = '')
    for draw in range(1, size+4): 
        start_space -= 1
        spaces = start_space* SPACE
        print(TOP_INITIAL_SPACE* SPACE, '|', spaces, draw*'/', SPACE,
               draw*'\\', spaces, '|', sep = '')

def draw_clock_tower(size:int, num_floors:int) -> None:
    '''
    prints a completed image of a clocktower given the size and number of
    floors of the tower
    
    Precondition: size and floors >=0
    '''
    draw_face(size)
    draw_top(size)
    draw_base(size, num_floors)
    