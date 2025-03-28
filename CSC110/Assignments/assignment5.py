import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

ONE_MATCH_ODDS = 1
TWO_MATCH_ODDS = 2
THREE_MATCH_ODDS = 10
ZERO_MATCH_ODDS = 1

def digit_sum(integer:int) -> int: #ERROR
    '''
    returns the sum of each digit in a given int (ignores negatives)
    
    >>> digit_sum(0)
    0
    >>> digit_sum(432)
    9
    >>> digit_sum(-571)
    13
    '''
    num_sum = 0
    pos_int = abs(integer)
    
    while pos_int >0:
        last_val = pos_int % 10
        num_sum += last_val
        pos_int = pos_int // 10
    
    return num_sum
        
def gcd(n1:int, n2:int) -> int:
    '''
    returns the greatest commmon divisor of n1 and n2
    
    Precondition: n1 and n2 > 0
    
    >>> gcd(1, 2)
    1
    >>> gcd(4, 7)
    1
    >>> gcd(12, 18)
    6
    '''
    smallest = min(n1, n2)
    
    while n1 % smallest > 0 or n2 % smallest > 0:
        smallest -= 1
    
    return smallest
               
def roll_one_die() -> int:
    ''' 
    simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value
    '''
    die = random.randint(MIN_ROLL, MAX_ROLL)
    return die

def play_again() -> bool:
    '''
    prompts player to enter whether they want to play again
    returns True if yes, False if anything else
    '''
    prompt = 'Do you want to make a bet? (yes/no): '
    response = input(prompt)
    
    if response == 'yes':
        return True
    else:
        return False
    
def get_guess() -> int:
    '''
    repeatedly prompts player for valid guess, returns guess if given
    
    Precondition: user enters an int and 1 <= int <= 6
    '''
    prompt = 'Guess a whole number between from 1 to 6: '
    guess = input(prompt)
    
    while not guess.isdigit() or int(guess) < MIN_ROLL or int(guess) > MAX_ROLL:
        guess = input(prompt)
    
    return int(guess)
    
def get_bet(bet_max:int) -> int:
    '''
    repeatedly prompts player for valid bet and returns the valid bet
    
    Precondition: bet_max is in and bet_max >= MIN_BET
    Precondition: user enters integer bet and MIN_BET <= bet <= bet_max
    '''
    prompt = f'Enter a wager between {MIN_BET} and {bet_max}: '
    wager = input(prompt)
    
    while not wager.isdigit() or int(wager) < MIN_BET or int(wager) > bet_max:
        wager = input(prompt)
    
    print(f'You bet ${wager}')
    return int(wager)

def roll_dice(guess:int) -> int:
    '''
    simulates the roll of three dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the number of dice rolls that match the given guess
    
    Precondition: 1 <= guess <= 6 and guess is int
    '''
    correct_guesses = 0
    
    for rolls in range(3):
        dice_roll = roll_one_die()
        print(f'Dice roll {rolls}: {dice_roll}')
        if int(dice_roll) == guess:
            correct_guesses += 1    
    
    return correct_guesses

def compute_winnings(match:int, bet:int) -> int:
    '''
    returns the player winnings or losses given the number of correct guesses
    and the previous wager
    
    Precondition: 0 <= match <=3 and match is int
    Precondition: MIN_BET <= bet and bet is int
    '''
    if match == 1:
        winnings = bet * ONE_MATCH_ODDS
        print(f'Congrats! You won ${winnings}')
    elif match == 2:
        winnings = bet * TWO_MATCH_ODDS
        print(f'Congrats! You won ${winnings}')
    elif match == 3:
        winnings = bet * THREE_MATCH_ODDS
        print(f'Congrats! You won ${winnings}')
    else:
        winnings = bet * ZERO_MATCH_ODDS
        print(f'Ah shucks... You lost ${winnings}')
        winnings *= -1
    
    return winnings
    
def play_one_round(bet:int) -> int:
    '''
    simulates one round of betting and dice rolling and returns the player 
    winnings or losses given the previous wager
    
    Precondition: MIN_BET <= bet and bet is int
    '''
    guess = int(get_guess())
    correct_guesses = roll_dice(guess)
    winnings = compute_winnings(correct_guesses, bet)
    
    return winnings

def play_game(start_cash:int) -> int:
    '''
    simulates multiple rounds of betting and dice rolling
    repeatedly asks player if they want to keep playing if total_cash >= 
    MIN_BET, otherwise prints bankroll
    
    Precondition: MIN_BET <= total_cash 
    '''
    print(f'You have ${start_cash} to play with')
    
    player_money = start_cash
    play = play_again()
    
    while play == True:
        bet = int(get_bet(player_money))
        winnings = play_one_round(bet)
        
        if type(winnings) == int:
            player_money += winnings
        else:
            end = len(winnings) 
            player_money -= int(winnings[1:end])
        
        print(f'You have ${player_money} in your bankroll')
        
        if player_money >= MIN_BET:
            play = play_again()
        else:
            return player_money
    
    print(f'You have ${player_money} in your bankroll')
    return player_money