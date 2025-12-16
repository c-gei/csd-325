## Cece Geisler
## CSD325
## Assignment 3.2
## 12/16/2025

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
Modified by CJG to meet assignment requirements.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

## Double tags are used to indicate changes made to the original code.

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
If the total of the dice roll is 2 or 7, you will receive a 10 mon bonus!
''') ## CHANGE 1: Added bonus information to the game description.

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
    ## CHANGE 2: Input prompt changed to initials (cjg)
        pot = input('cjg: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
    ## CHANGE 2: Input prompt changed to initials (cjg)
        bet = input('cjg: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    ## CHANGE 4: Bonus logic implemented
    roll_total = dice1 + dice2
    if roll_total == 2 or roll_total == 7:
        print(f'*** Bonus! You rolled a {roll_total}. You get a 10 mon bonus! ***') 
        purse = purse + 10  ## Adding the bonus to the purse.

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        
    ## CHANGE 3: House fee changed to 12%
        fee = int(pot * 0.12)
        print('The house collects a', fee, 'mon fee (12% of bet).')
        purse = purse - fee

    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()

## END