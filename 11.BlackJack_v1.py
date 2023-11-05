# BlackJack

import random
import blackjack

play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

while play == 'y':
    print(blackjack.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = []
    pos1 = random.randint(0, 12)
    card1 = cards[pos1]
    pos2 = random.randint(0, 12)
    card2 = cards[pos2]
    your_cards += list(f"{card1}")+list(f"{card2}")
    current_score = card1+card2
    print(f"\tYour cards: {your_cards}, current score: {current_score}")
    comp_cards = []
    com_pos1 = random.randint(0, 12)
    comp_card1 = cards[com_pos1]
    comp_pos2 = random.randint(0, 12)
    comp_card2 = cards[comp_pos2]
    comp_cards += list(f"{comp_card1}") + list(f"{comp_card2}")
    comp_score = comp_card1+comp_card2
    print(f"\tComputer's first card: {comp_card1}")

    get_card = True
    while get_card:
        if current_score <= 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                another_pos = random.randint(0, 12)
                another_card = cards[another_pos]
                your_cards += list(f"{another_card}")
                current_score += another_card
                print(f"\tYour cards: {your_cards}, current score: {current_score}")
            else:
                get_card = False
        else:
            get_card = False

    print(f"Your final hand: {your_cards}, final score: {current_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")

    if current_score > 21:
        print("You went over. You lose")
    else:
        while comp_score < 17:
            another_comp_pos = random.randint(0, 12)
            another_comp_card = cards[another_comp_pos]
            comp_cards += list(f"{another_comp_card}")
            comp_score += another_comp_card
            print(f"\tComp cards: {comp_cards}, current score: {comp_score}")
        if current_score == comp_score:
            print("It is a draw.")
        elif current_score > comp_score:
            print("Congratulations! You win")
        elif comp_score > 21:
            print("Congratulations! You win")
        else:
            print("You lose. Better luck next time.")

    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
