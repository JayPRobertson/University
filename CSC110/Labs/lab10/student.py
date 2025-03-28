import doctest

class Student:
    """ Student with unique id (sid) and current grade (grade)"""

    def __init__(self, sid: str, grade: int) -> None:
        """ initializes an instance of a Student with sid and grade
        >>> stdnt = Student('V00123456', 89)
        """
        self.__sid = sid
        self.__grade = grade

    def __str__(self) -> str:
        """ return a formatted string with sid and grade of self Student
        >>> stdnt = Student('V00123456', 89)
        >>> str(stdnt)
        'V00123456: 89/100'
        """
        return f'{self.__sid}: {self.__grade}/100'

    def __repr__(self) -> str:
        """ return a formatted string  with student attributes
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt
        Student('V00123456', 89)
        """        
        return f'Student({repr(self.__sid)}, {repr(self.__grade)})'
    
    def __eq__(self, other:'Student') -> bool:
        '''
        compares the sids of two Student instances; returns True if they are
        the same and False otherwise
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt2 = Student('V00654321', 24)
        >>> stdnt3 = Student('V00123456', 12)
        
        >>> stdnt1 == stdnt2
        False
        >>> stdnt1 == stdnt3
        True
        >>> stdnt2 == stdnt3
        False
        '''
        return self.__sid == other.__sid
    
    def is_grade_above(self, thresh_grade:int) -> bool:
        '''
        determines whether value of the grade of Student self  is greater than
        a given threshold grade (thresh_grade)
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1.is_grade_above(76)
        True
        >>> stdnt1.is_grade_above(97)
        False
        >>> stdnt1.is_grade_above(89)
        False
        '''
        return self.__grade > thresh_grade
    
    def get_sid(self) -> str:
        '''
        returns the value of sid for Student self
        
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.get_sid()
        'V00123456'
        '''
        return self.__sid

    def get_grade(self) -> int:  
        '''
        returns the value of grade for Student self
        
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.get_grade()
        89
        '''
        return self.__grade

    def set_grade(self, grade):
        '''
        changes or sets the value of grade for Student self
        
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.set_grade(64)
        >>> stdnt
        Student('V00123456', 64)
        '''
        self.__grade = grade