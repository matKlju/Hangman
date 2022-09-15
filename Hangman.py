

import random
from words import words

guessed_word = []
guessed_letters = [] #
word = [i for i in random.choice(words) for y in i] # random word to guess

for i in range(len(word)):
    guessed_word.append('__') # word interface. '__' as unguessed letters

tries_left = len(word) * 2 # tries left 
while '__' in guessed_word: # loop keeps going while it still has '__'
    
    # State of game 
    print(f'Guessed letters: {guessed_letters} count: {len(guessed_letters)}\n\
Tries left: {tries_left}\nWord: {guessed_word}')
   
    # If tries over = game over
    if tries_left == 0:
        print(f'\nYou LOST! Out of tries.\nThe word was: {word}')
        exit()
        
    # guess letter  
    guess = input('\nGuess one letter: ')
    
    if len(guess) > 1:    # if letter too short, restart loop
        print('Too long! One letter only!')
        
    elif guess in word:   # if letter occurs in word, start check
        index_count = -1
        
        for i in word:    # iterate through word, check for letters
            index_count += 1
            
            if str(i) == guess:    # index_count to print reoccurring letters
                guessed_word[index_count] = guess
    
    else:    # when wrong letter then else block
        print('No such letter in word')
        guessed_letters.append(guess)
        tries_left -= 1
    
    # if no '__' in guessed_word, loop ends and game won!
print('\nYou WON!')
print(f'Word: {guessed_word}')

