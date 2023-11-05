# Guess the number

import random
from guessthenumber import logo

# Welcome texts and selecting 1 number
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
num_range = []
for i in range(1, 101):
    num_range.append(i)

number = random.choice(num_range)


def guess():
    guess_num = int(input("Make a guess: "))
    if guess_num > number:
        return "high"
    elif guess_num < number:
        return "low"
    else:
        return "win"


difficulty = input("Choose a difficulty. Type 'easy' for easy or 'hard' for hard: ").lower()
if difficulty == 'easy':
    lives = 10
    print("You have 10 attempts to guess this number")
else:
    lives = 5
    print("You have 5 attempts to guess this number")
can_continue = True

while can_continue and lives > 0:
    guess_ans = guess()
    if guess_ans == 'win':
        print("You guessed it right. You win!")
        can_continue = False
    else:
        print(f"Too {guess_ans}")
        lives -= 1

if lives < 1:
    print("Sorry you have ran out of guesses. You lose")
