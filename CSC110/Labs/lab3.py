import doctest

GST = 0.05
PST = 0.1

def get_longer(phrase1:str, phrase2:str) -> str:
    '''
    compares phrase1 and phrase2 and returns the longer of the two
    if same length, first argument is returned
    
    >>> get_longer('my', 'name')
    'name'
    >>> get_longer('hello', 'mom')
    'hello'
    >>> get_longer('hello', 'world')
    'hello'
    '''
    if len(phrase1) >= len(phrase2):
        return phrase1
    else:
        return phrase2 

def get_tax(food_cost:float, alcohol_cost:float) -> float:
    '''
    returns the tax owed on food and alcohol charges
    Precondition: food_cost and alcohol_cost >=0 and are in dollars
   
    >>> get_tax(14.99, 6.45)
    1.717
    >>> get_tax(0, 0)
    0.0
    >>> get_tax(25.99, 0)
    1.2995
    '''
    food_tax = food_cost * GST
    
    alcohol_gst = alcohol_cost * GST
    alcohol_pst = alcohol_cost * PST
    total_alcohol_tax = alcohol_gst + alcohol_pst
    
    total_tax = total_alcohol_tax + food_tax
    return total_tax

def get_bill_share(food_cost:float, alcohol_cost:float, 
                   num_people: int) -> float:
    '''
    returns the cost for food and alcohol, with tax, evenly split 
    amongst a group
    
    Precondition: food_cost and alcohol_cost >=0 and are in dollars
    Precondition: num_people >=1
    
    >>> get_bill_share(14.99, 6.45, 3)
    7.719
    >>> get_bill_share(0, 0, 5)
    0.0
    >>> get_bill_share(25.99, 0, 3)
    9.096499999999999
    >>> get_bill_share(25.99, 45.00, 1)
    79.03949999999999
    '''
    tax_cost = get_tax(food_cost, alcohol_cost)
    total_cost = food_cost + alcohol_cost + tax_cost
    bill_share = total_cost/num_people
    return bill_share