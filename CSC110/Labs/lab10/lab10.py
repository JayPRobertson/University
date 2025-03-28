import doctest
from student import Student

#position in csv file
SID = 0
GRADE = 1

def get_students(filename:str) -> list[Student]:
    '''
    returns a list of Student object information in filename
    
    Precondition: filename exists and data is organized where each line of 
    the file has a unique student id and grade separated by a comma
    
    >>> get_students('empty.txt')
    []
    >>> get_students('student_data.csv')
    [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    '''
    new_list = []
    
    filehandle = open(filename, 'r')
    for line in filehandle:
        line = line.strip()
        line = line.split(',')
        
        student = Student(line[SID], int(line[GRADE]))
        new_list.append(student)
        
    filehandle.close()
    return new_list

def get_classlist(lostudents:list[Student]) -> list[str]:
    '''
    returns a list of all student ids in lostudents 
    Precondition: all ids in lostudents are unique
    
    >>> get_classlist([])
    []
    >>> lostudents = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> get_classlist(lostudents)
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    '''
    new_list = []
    
    for student in lostudents:
        sid = student.get_sid()
        new_list.append(sid)
    
    return new_list

def count_above(lostudents:list[Student], thresh_grade:int) -> int:
    '''
    returns the number of students in lostudents above thresh_grade
    
    >>> count_above([], 1)
    0
    
    >>> lostudents = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> count_above(lostudents, 10)
    4
    >>> count_above(lostudents, 80)
    2
    >>> count_above(lostudents, 99)
    0
    '''
    count = 0
    for student in lostudents:
        is_above = student.is_grade_above(thresh_grade)
        if is_above:
            count += 1
    
    return count

def get_average_grade(lostudents:list[Student]) -> float:
    '''
    returns the average grade of all Students in lostudents as a float
    Precondition: lostudents != []
    
    >>> get_average_grade([])
    0.0
    
    >>> lostudents = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> get_average_grade(lostudents)
    74.0
    '''
    grade_sum = 0
    
    if lostudents == []:
        return 0.0
    
    for student in lostudents:
        grade = student.get_grade()
        grade_sum += grade
    
    grade_avg = grade_sum/len(lostudents)
    return grade_avg      