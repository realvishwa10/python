# HANGMAN

import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)

# Selecting a random word for the game
word_list = ["mouse", "cat", "dog", "cow", "fish", "parrot"]
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

# Displaying number of blanks
guess_word = []
for index in range(len(chosen_word)):
    guess_word += "_"
print(guess_word)

end_of_game = False
already_tried = []
wrong_words_chosen = []

while not end_of_game:
    # Get input and check Right/Wrong
    guess = input("Guess a letter: ").lower()
    if guess in already_tried:
        print("Already tried this letter")
    else:
        already_tried_list = already_tried.append(guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                guess_word[position] = guess
                print(guess_word)
        if guess not in chosen_word:
            lives -= 1
            wrong_words = wrong_words_chosen.append(guess)
            print(wrong_words)
            print(stages[lives])
            if lives <= 0:
                end_of_game = True
                print("Sorry. You have lost")

        if "_" not in guess_word:
            end_of_game = True
            print(f"{guess_word} is the correct word. You win!")
