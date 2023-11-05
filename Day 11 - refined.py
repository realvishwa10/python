import random
from blackjack import logo


def deal_card():
    """ Picks a random card"""
    dealers_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(dealers_cards)


def calculate_score(cards):
    """ Takes a list of cards and returns the sum of the cards in list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It is a draw 😐"
    elif c_score == 0:
        return "Dealer wins by hitting BlackJack 😱"
    elif u_score == 0:
        return "You win by hitting BlackJack 😱"
    elif u_score > 21:
        return "You went over. You lose ☹"
    elif c_score > 21:
        return "You win!! 😎"
    elif u_score > c_score:
        return "You win!! 😎"
    else:
        return "Sorry. You lose ☹"


def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"    Your cards are: {user_cards}, current_score: {user_score}")
        print(f"    Computer first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
