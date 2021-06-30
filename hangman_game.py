import easy, medium, difficult
import random
import sys
import os
import time
from hangman_stages import hangman


def clear_screen():
    '''Utility to Clear Screen on different platforms'''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def show_game_banner():
    print('THE HANGMAN GAME')
    print('================')
    print('')
    
    
while True:
    # welcome screen for user
    show_game_banner()
    def menu(subject, options):
        '''Display Menu based on parameters'''
        print('Please choose ' + subject)
        options_count = len(options.keys())
        for num, value in options.items():
            print(f'{num}. {value}')
        choice = int(input(f'Your choice (1-{options_count}): '))
        return choice

    # select difficulty
    DIFFICULTY = menu('Difficulty', {1: 'Easy', 2: 'Medium', 3: 'Difficult'})
    
    # select number of turns
    NUMBER_OF_TURNS = [12, 6, 3][DIFFICULTY-1]
    
    # select hangman_stage_jumper: decides how many stages to skip based on difficulty
    HANGMAN_STAGE_JUMPER = [1, 2, 4][DIFFICULTY-1]
    CURRENT_STAGE = 1
    
    # select word
    WORD = random.choice([easy.words, medium.words, difficult.words][DIFFICULTY-1]).upper()
    LETTERS_YET_TO_BE_GUESSED = set(WORD) # utility for storing letters remining to be guessed
    
    ALREADY_GUESSED_LETTERS = set() # utility for storing already guessed letters
    
    clear_screen()
    
    # start game - loop 
        # check if turns > 0
        # check letters yet to be guessed exist
    while LETTERS_YET_TO_BE_GUESSED and NUMBER_OF_TURNS > 0:
        show_game_banner()
        # Sample Screen view:
            # Turns remaining: 6
            # Hangman goes here
            # * * * * * * * *
            # Already Guessed:
            # New Guess:
        print('Turns remaining: ' + str(NUMBER_OF_TURNS))
        # show word - hide letters not yet guessed
        WORD_SO_FAR = [letter if letter in ALREADY_GUESSED_LETTERS else '*' for letter in WORD]
        print(hangman[CURRENT_STAGE])
        print(' '.join(WORD_SO_FAR))
        print('Already Guessed: ' + ' '.join(ALREADY_GUESSED_LETTERS))

        GUESSED_LETTER = input('New Guess: ').upper()
        if GUESSED_LETTER in LETTERS_YET_TO_BE_GUESSED:
            LETTERS_YET_TO_BE_GUESSED.remove(GUESSED_LETTER)
            ALREADY_GUESSED_LETTERS.add(GUESSED_LETTER)
        elif GUESSED_LETTER in ALREADY_GUESSED_LETTERS:
            print('You have guessed this letter already.')
            time.sleep(2)
        else:
            ALREADY_GUESSED_LETTERS.add(GUESSED_LETTER)
            NUMBER_OF_TURNS -= 1
            CURRENT_STAGE += HANGMAN_STAGE_JUMPER
        clear_screen()

    if NUMBER_OF_TURNS == 0:
        show_game_banner()
        print(hangman[12])
        print('Hangman DIED!')
        print('Game Over. You Lost :(')
    else:
        print('You Guesses it, Right!! Hangman is saved!')
    print('The word is : ' + WORD)
    
    choice = input('Press any key to continue, or press q to quit.')
    if choice in ['q', 'Q']:
        break
    clear_screen()