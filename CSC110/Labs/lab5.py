import doctest

ADULT_MIN_AGE = 18
SENIOR_MIN_AGE = 65

PROMPT1 = 'type name: '
PROMPT2 = 'type age: '

def print_name_age_v1() -> None:
    '''
    prints a message when a user enters valid name and age to the shell
    
    Precondition: user enters an int number >=0 
    '''
    name = input(PROMPT1)
    age = int(input(PROMPT2))
    
    if age >= SENIOR_MIN_AGE:
        age_type = 'senior'
    elif age < ADULT_MIN_AGE:
        age_type = 'child'
    else:
        age_type = 'adult'
    
    print('hello', name, age_type)
#an error message will print if an invalid age is entered
    
def print_name_age_v2() -> None:
    '''
    prints a message when a user enters valid name and age to the shell
    if the user enters a negative number or invalid number not an int, 
    prints a message
    '''
    name = input(PROMPT1)
    age = input(PROMPT2)
    is_digit = age.isdigit()
    
    if is_digit == True:
        age = int(age)
        if age < 0:
            print(name,'you are lying about your age')
        elif age >= SENIOR_MIN_AGE:
            age_type = 'senior'
        elif age < ADULT_MIN_AGE:
            age_type = 'child'
        else:
            age_type = 'adult'
        print('hello', name, age_type) 
    else:
        print(name,'you are lying about your age')
    

def get_num(min_num:int, prompt:str) -> int:
    '''
    repeatedly prompts user to enter number, returns given value as int
    if the user enters a negative number or invalid number not an int, then
    prompt again
    
    Precondition: number user enters >= min_num
    '''
    num_str = input(prompt)
    
    while not num_str.isdigit() or int(num_str) < min_num:
        num_str = input(prompt)
    num = int(num_str)
    return num

def print_name_age_v3() -> None:
    '''
    prints a message when a user enters valid name and age to the shell
    if the user enters a negative number or invalid number not an int, then
    prompt again
    '''  
    name = input(PROMPT1)
    age = get_num(0, PROMPT2)
    if age >= SENIOR_MIN_AGE:
        age_type = 'senior'
    elif age < ADULT_MIN_AGE:
        age_type = 'child'
    else:
        age_type = 'adult'
    print('hello', name, age_type)