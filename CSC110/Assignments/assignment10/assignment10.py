import doctest
from pet import Pet
from date import Date

# represents a pet as (name, species)
PetNameSpecies = tuple[str,str]

# columns of values within input file row and within PetNameSpecies tuple
NAME    = 0
SPECIES = 1
MONTH   = 2
DAY     = 3
YEAR    = 4

#positions of different pets in a list of Pets (list[Pet])
FIRST_PET = 0

def read_file(filename: str) -> list[Pet]:
    ''' returns a list of Pets populated with data from filename
    
    Preconditions: filename exists.
    If filename is not empty, each row has a single Pet's information
    separated by commas with expected values at columns:
    NAME, SPECIES, MONTH, DAY and YEAR.

    >>> read_file('empty.csv')
    []
    >>> read_file('pet_data.csv')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    '''
    new_list = []
    
    filehandle = open(filename, 'r')
    for line in filehandle:
        line = line.strip()
        line = line.split(',')
        
        date_obj = Date(int(line[MONTH]), int(line[DAY]), int(line[YEAR]))
        pet_obj = Pet(line[NAME], line[SPECIES], date_obj)
        new_list.append(pet_obj)
        
    filehandle.close()
    return new_list

def find_pet(lopets: list[Pet], name: str) -> int:
    ''' returns the position of pet with given name in lopets
    Returns -1 if name not found
    Returns the position of the first found if there >1 Pet with the given name
    
    Precondition: name must match case exactly
    ie. 'rover' does not match 'Rover'

    >>> find_pet([], 'Fred')
    -1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Bowser')
    -1
    >>> find_pet([Pet('Red', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    0
    '''
    index = 0
    
    while index < len(lopets):
        cur_pet = lopets[index]
        cur_name = cur_pet.get_name()
        if cur_name == name:
            return index
        index += 1
    
    return -1
    
def get_all_of_species(lopets: list[Pet], species: str) -> list[Pet]:
    ''' returns a list of all pets of the given species.
    Result list is not necessarily unique, if >1 Pet in lopets has the same name.
    
    Precondition: species must match case exactly
    ie. 'dog' does not match 'Dog'
    
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_all_of_species([], 'Dog')
    []
    >>> get_all_of_species(pets, 'Dog')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_all_of_species(pets, 'Tiger')
    []
    >>> get_all_of_species(pets, 'Hamster')
    [Pet('Chewie', 'Hamster', Date(1, 23, 2009))]
    '''
    new_list = []
    
    for pet_object in lopets:
        cur_species = pet_object.get_species()
        if cur_species == species:
            new_list.append(pet_object)
            
    return new_list


def get_latest_birthdate(lopets: list[Pet]) -> Date:
    ''' returns the latest Date of all birthdates of Pet instances in lopets
    Precondition: lopets is not empty
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_latest_birthdate([Pet('Rover', 'Dog', Date(12, 31, 2010))])
    Date(12, 31, 2010)
    >>> get_latest_birthdate(pets)
    Date(9, 15, 2016)
    '''
    latest_date = ''
    
    for index in range(len(lopets)):
        cur_pet = lopets[index]
        cur_date = cur_pet.get_birthdate()
        
        if index == 0 or cur_date.is_after(latest_date):
            latest_date = cur_date
            
    return latest_date
                

def get_youngest_pets(lopets: list[Pet]) -> list[PetNameSpecies]:
    ''' returns a list of PetNameSpecies of all the youngest pets in lopets
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_youngest_pets([])
    []
    >>> get_youngest_pets(pets)
    [('Red', 'Cat'), ('Scout', 'Dog')]
    '''
    pets_object_list = []
    pets_list = []
    
    if lopets != []:
        for pet_object in lopets:
            cur_birthdate = pet_object.get_birthdate()
            cur_pet = pet_object.get_name()
            cur_species = pet_object.get_species()
            
            if pets_object_list == [] or cur_birthdate.is_after(\
                                pets_object_list[FIRST_PET].get_birthdate()):
                pets_object_list = [pet_object]
                pets_list = [(cur_pet, cur_species)]
                
            elif cur_birthdate == pets_object_list[FIRST_PET].get_birthdate():
                pets_object_list.append(pet_object)
                pets_list.append((cur_pet, cur_species))
        
    return pets_list