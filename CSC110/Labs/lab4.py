import doctest

def compute_harmonic_series(n:int) -> float:
    '''
    returns the sum of a harmonic series up to n
    Precondition: n >= 0
    
    >>> compute_harmonic_series(5)
    2.283333333333333
    >>> compute_harmonic_series(10)
    2.9289682539682538
    >>> compute_harmonic_series(0)
    0
    >>> compute_harmonic_series(1)
    1.0
    '''
    harmonic_sum = 0
    for series in range(1, n+1):
        harmonic_sum += 1/series 
    return harmonic_sum

def get_fibonacci_sequence(n:int) -> str:
    '''
    returns a string of the first n values of the fibonacci sequence
    Precondition: n >= 0
    
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(2)
    '0,1'
    >>> get_fibonacci_sequence(9)
    '0,1,1,2,3,5,8,13,21'
    '''
    previous_num = 0
    current_num = 1
    new_sequence = ''
    
    if n==0:
        return new_sequence
    elif n==1:
        return str(previous_num)
    elif n==2:
        return '0,1'
    else: 
        for sequence in range(2,n):    
            next_num = previous_num + current_num
            previous_num = current_num
            current_num = next_num
            next_num = str(next_num)
            if sequence < n:
                new_sequence = new_sequence + ',' + next_num 
            else:
                new_sequence = new_sequence + next_num
        return '0,1' + new_sequence    

def print_pattern(height:int, width:int, str1:str, str2:str) -> None:
    '''
    prints a pattern based on the height and width of the rows and the 
    str characters that make up the pattern
    
    Precondition: height and width > 0
    
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    
    >>> print_pattern(2,4, '~<>~', '(-)')
    ~<>~(-)~<>~(-)~<>~(-)~<>~(-)
    (-)~<>~(-)~<>~(-)~<>~(-)~<>~
    
    >>> print_pattern(1,1, '><><', '00')
    ><><00
    '''
    for pattern in range(height):
            if pattern%2 == 0:
                for row in range(width):
                    print(str1, str2, sep='', end='')
            else:
                for row in range(width):
                    print(str2, str1, sep='', end='')
            print('')    