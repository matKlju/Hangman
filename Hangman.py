

"""

Hangman GUI

Developing simple GUI for hangman game

To do:
    implement basic GUI - done

"""

import PySimpleGUI as sg
from random import choice as rnd
from words import words

guessed_word = []
guessed_letters = []

word = [i for i in rnd(words) for y in i]  # random word to guess

for i in range(len(word)):
    guessed_word.append('__')  # word interface. '__' as guessed letters

tries_left = len(word) * 2  # tries left
while '__' in guessed_word:  # loop keeps going while it still has '__'
    
    # State of game, guess letter
    layout = [
        [sg.Text(
            f'Guessed letters: {guessed_letters}\ncount: {len(guessed_letters)}\n\n'
            f'Tries left: {tries_left}\nWord: {guessed_word}\nGuess one letter:')],
        [sg.InputText()],
        [sg.Ok()]
    ]

    window = sg.Window('Hangman', layout)
    value = window.read()
    window.close()

    guess = (value[1])[0]

    # If tries over = game over
    if tries_left == 0:
        sg.popup(f'\nYou LOST! Out of tries.\nThe word was: {word}')
        exit()

    if len(guess) > 1:    # if letter too short, restart loop
        sg.popup('Too long! One letter only!')
        
    elif guess in word:   # if letter occurs in word, start check
        index_count = -1
        
        for i in word:    # iterate through word, check for letters
            index_count += 1
            
            if str(i) == guess:    # index_count to print reoccurring letters
                guessed_word[index_count] = guess
    
    else:    # when wrong letter then else block
        sg.popup('No such letter in word')
        guessed_letters.append(guess)
        tries_left -= 1
    
    # if no '__' in guessed_word, loop ends and game won!

sg.popup(f'\nYou WON!\nWord: {guessed_word}')
