import doctest


class Date:
    """ Date: represents a date in the Gregorian calendar used worldwide.
    Precondition, month, day, year must make a valid calendar date.
    """

    def __init__(self, month: int, day: int, year: int) -> None:
        """ initializes attributes of Date instance
        >>> dt = Date(12, 19, 2020)
        """
        self.__month = month
        self.__day = day
        self.__year = year

    def get_month(self) -> int:
        """ returns month of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_month()
        12
        """
        return self.__month

    def get_day(self) -> int:
        """ returns day of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_day()
        19
        """
        return self.__day

    def get_year(self) -> int:
        """ returns year of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_year()
        2020
        """
        return self.__year

    def __str__(self) -> str:
        """ returns a readable string with month, day, year of Date
        >>> dt = Date(12, 19, 2020)
        >>> str(dt)
        '12-19-2020'
        """
        return f'{self.__month}-{self.__day}-{self.__year}'

    def __repr__(self) -> str:
        """ returns a string representation of self Date
        >>> dt = Date(12, 19, 2020)
        >>> repr(dt)
        'Date(12, 19, 2020)'
        """
        return f'Date({repr(self.__month)}, {repr(self.__day)}, {repr(self.__year)})'

    def __eq__(self, other: 'Date') -> bool:
        """ returns True if self Date has same month, day, year as
        other Date, otherwise False
        >>> dt12192020a = Date(12, 19, 2020)
        >>> dt12192020b = Date(12, 19, 2020)
        >>> dt12192021  = Date(12, 19, 2021)
        >>> dt12182020  = Date(12, 18, 2020)
        >>> dt11192020  = Date(11, 19, 2020)

        >>> dt12192020a == dt12192020a
        True
        >>> dt12192020a == dt12192020b
        True
        >>> dt12192020a == dt12192021
        False
        >>> dt12192020a == dt12182020
        False
        >>> dt12192020a == dt11192020
        False
        """
        return (self.__month == other.__month
                and self.__day == other.__day
                and self.__year == other.__year)
    
    def is_after(self, other:'Date') -> bool:
        ''' 
        returns True if self Date is after other Date in the calender and 
        False otherwise
        
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(12, 19, 2020)
        >>> dt3 = Date(12, 19, 2022)
        >>> dt4 = Date(6, 8, 2019)
        
        >>> dt1.is_after(dt3)
        False
        >>> dt1.is_after(dt4)
        True
        >>> dt1.is_after(dt2)
        False
        '''
        return self.get_year() > other.get_year() \
            or (self.get_year() == other.get_year() 
            and (self.get_month() > other.get_month() 
                or (self.get_month() == other.get_month() 
                and self.get_day() > other.get_day())))
        
                
        
        




