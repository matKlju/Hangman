"""

Hangman game

"""

from sys import exit as sys_exit
from random import choice as rnd
import urllib.request

WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"

with urllib.request.urlopen(WORD_SITE) as f:
    data = f.read()

WORDS = tuple(str(i)[2:-1] for i in data.splitlines() if len(str(i)[2:-1]) > 3)


def display_noose(value):
    """Display hanging stage depending tries"""

    if value == 7:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||\n  ||\n  ||\n /||\\\n/_||_\\\n')

    elif value == 6:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||\n  ||\n /||\\\n/_||_\\\n')

    elif value == 5:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||      |\n  ||\n /||\\\n/_||_\\\n')

    elif value == 4:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||     /|\n  ||\n /||\\\n/_||_\\\n')

    elif value == 3:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||     /|\\\n  ||\n /||\\\n/_||_\\\n')

    elif value == 2:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||     /|\\\n  ||      |\n /||\\\n/_||_\\\n')

    elif value == 1:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||     /|\\\n  ||      |\n /||\\    /\n/_||_\\\n')

    elif value == 0:
        print('   _______\n  ||      |\n  ||      |\n'
              '  ||      0\n  ||     /|\\\n  ||      |\n /||\\    / \\\n/_||_\\\n')


def display_status(limit, wrong_letters, hidden_word):
    """Display current game status"""

    print(f'Tries left: {limit}\nWrong letters: {wrong_letters}\n'
          f'Guess the word: {hidden_word}')


def guess_word(word_to_guess):
    """Let user guess word. Evaluate and return result"""

    hidden_word = ['_' for _ in word_to_guess]
    wrong_letters = []
    limit = 7

    while True:
        try:
            display_noose(limit)
            display_status(limit, wrong_letters, hidden_word)
            letter = input('\tLetter: ')

        except ValueError:
            print('Only letters!')
            continue

        if letter not in word_to_guess:
            limit -= 1
            wrong_letters.append(letter)
            print('\nNo such letter in word\n')

            if limit < 1:
                display_noose(limit)
                print(f'Out of tries!\n\nThe word was "{word_to_guess}"\n')
                return False
            continue

        for index, value in enumerate(list(word_to_guess)):
            if value == letter:
                hidden_word.pop(index)
                hidden_word.insert(index, letter)

        if hidden_word == list(word_to_guess):
            return True


def game():
    """Main game"""

    word_to_guess = rnd(WORDS)

    if guess_word(word_to_guess):
        print('\nYou win!\n')
    else:
        print("\nYou have lost! Now your feet don't touch the ground\n")


def main():
    """Main menu 1 start game, 2 quit"""

    while True:
        try:
            choice = int(input('(1) Play HANGMAN\n(2) Exit\n\t: '))
        except ValueError:
            print('Only number values! ')
            continue

        if choice < 1 or choice > 2:
            print('Only choose 1 or 2')
            continue
        if choice == 1:
            game()
        else:
            print('Bye!')
            sys_exit()


if __name__ == '__main__':
    main()
