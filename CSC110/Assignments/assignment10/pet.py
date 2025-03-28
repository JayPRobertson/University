import doctest
from date import Date

class Pet:
    """ Pet: represents a domesticated pet with name, species and birthdate """

    def __init__(self, name: str, species: str, birthdate: Date) -> None:
        """ initializes attributes of Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        """
        self.__name      = name
        self.__species   = species
        self.__birthdate = birthdate

    def get_name(self) -> str:
        """ returns name of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_name()
        'Rover'
        """
        return self.__name

    def get_species(self) -> str:
        """ returns species of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_species()
        'Dog'
        """
        return self.__species
    
    def get_birthdate(self) -> Date:
        """ returns date of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        
        >>> dog.get_birthdate()
        Date(12, 19, 2020)
        """
        return self.__birthdate
    
    def __str__(self) -> str:
        """ returns a readable string with name, species, birthdate of Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> str(dog)
        'Rover is a Dog. Born: 12-19-2020'
        """
        return f'{self.__name} is a {self.__species}. Born: {self.__birthdate}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> repr(dog)
        "Pet('Rover', 'Dog', Date(12, 19, 2020))"
        """
        return f'Pet({repr(self.__name)}, {repr(self.__species)}, {repr(self.__birthdate)})'
    
    def __eq__(self, other:'Pet') -> bool:
        '''
        compares two Pet instances; returns True if the name, species, and 
        birthdate of both instances are the same and False otherwise
        
        >>> dt1 = Date(12, 19, 2021)
        >>> dt2 = Date(12, 19, 2020)
        >>> dt3 = Date(12, 31, 2020)
        
        >>> pet1 = Pet('Rover', 'Cat', dt1)
        >>> pet2 = Pet('Rover', 'Dog', dt2)
        >>> pet3 = Pet('Calle', 'Hamster', dt3)
        >>> pet4 = Pet('Calle', 'Hamster', dt1)
        
        >>> pet1 == pet2
        False
        >>> pet2 == pet2
        True
        >>> pet1 == pet4
        False
        >>> pet3 == pet4
        False
        '''
        return self.get_birthdate() == other.get_birthdate() \
               and self.get_name() == other.get_name() \
               and self.get_species() == other.get_species()