# ROCK PAPER SCISSOR GAME

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
selection = [rock, paper, scissor]

admin = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
if 0 < admin > 2:
    print("Wrong input. Game over")
else:
    print(selection[admin])
    print("Computer chose:")
    computer = random.randint(0, 2)
    print(selection[computer])

    if admin == computer:
        print("It's a draw")
    elif admin == 0 and computer == 2:
        print("You win!")
    elif admin == 1 and computer == 0:
        print("You win!")
    elif admin == 2 and computer == 1:
        print("You win!")
    else:
        print("You lose :(")
