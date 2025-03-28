import doctest

#represents the information for a person: tuple[person name, person age]
#Precondition: age >= 0
PersonInfo = tuple[str, int]

NAME = 0
AGE = 1

def file_to_person_list(file_name:str) -> list[PersonInfo]:
    '''
    reads the lines of given existing file and returns a list of tuples 
    containing the name and age of each person in the file
    
    Precondition: file_name formatted as the name of a person and their age
    as int separated by a space; one on each line
    
    >>> file_to_person_list('lab8-name-age.txt')
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), \
('Jingwen', 17), ('Rajan', 65)]
    '''
    list_people_info = []
    
    people_info = open(file_name, 'r')
    
    person_info = people_info.readline()
    while person_info != '':
        person_info = person_info.strip()
        person_info = person_info.split()
        person_info[AGE] = int(person_info[AGE])
        list_people_info.append(tuple(person_info))
        person_info = people_info.readline()
   
    people_info.close()
    return list_people_info

def get_average_age(people_info:list[PersonInfo]) -> int:
    '''
    returns the average age of all ages in given list as an int (round down)
    Precondition: list != []
    
    >>> get_average_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18)])
    17
    >>> get_average_age([('Jose', 1), ('Jingwen', 0), ('Rajan', 100)])
    33
    >>> get_average_age([('Callum', 29)])
    29
    '''
    total_ages = 0
    num_people = 0
    
    for person in people_info:
        age = person[AGE]
        total_ages += age
        num_people += 1
    
    if num_people != 0:
        avg_age = total_ages//num_people
        return avg_age

def get_above_age(people_info:list[PersonInfo],
                  threshold_age:int) -> list[PersonInfo]:
    '''
    returns a list of all PersonInfo in a given list containing an age > than
    the threshold age
    
    Precondition: threshold_age >= 0
    
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18)], 10)
    [('Tian', 27), ('Daljit', 18)]
    >>> get_above_age([('Jose', 1), ('', 0), ('Rajan', 100)], 101)
    []
    >>> get_above_age([], 5)
    []
    >>> get_above_age([], 0)
    []
    >>> get_above_age([('Russ', 11), ('Gill', 41), ('Pablo', 1)], 0)
    [('Russ', 11), ('Gill', 41), ('Pablo', 1)]
    '''
    older_list = []
    
    for person in people_info:
        age = person[AGE]
        if age > threshold_age:
            older_list.append(person)
            
    return older_list

def to_file(people_info:list[PersonInfo], file_name:str) -> None:
    '''
    writes the name and age from each PersonInfo in a given list on its own 
    line (separated by commas) in a given file
    
    Precondition: file_name exists
    
    >>> to_file([('Jose', 53), ('Rajan', 65)], 'SampleOutput-write_names_above_avg_age.csv')
    '''
    new_file = open(file_name, 'w')
    
    for person in people_info:
        name = person[NAME]
        age = person[AGE]
        num_chars = new_file.write(f'{name},{age}\n')
    
    new_file.close()
    

def write_names_above_avg_age(input_file:str, output_file:str) -> None:
    '''
    reads all from input_file and writes all names and ages > the average
    age of the people listed in the input_file
    
    Precondition: input_file exits and is formatted as person's name and their 
    age (as int) separated by a space, one on each line; output_file exists
    '''
    list_people_info = file_to_person_list(input_file)
    avg_age = get_average_age(list_people_info)
    list_above_age = get_above_age(list_people_info, avg_age) 
    to_file(list_above_age, output_file)