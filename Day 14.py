# Higher lower game

import higherlower
import random


def show_details(data):
    name = data['name']
    description = data['description']
    country = data['country']
    return f"{name}, {description}, {country}"


def compare(data1, data2):
    follower1 = data1['follower_count']
    follower2 = data2['follower_count']
    if follower1 > follower2:
        return 0
    else:
        return 1


print(higherlower.logo)

game_data = higherlower.data
score = 0
game_continue = True
another_data = random.choice(game_data)

while game_continue:
    first_data = another_data
    print(f"Compare A: {show_details(first_data)}")
    print(higherlower.vs)
    another_data = random.choice(game_data)
    print(f"Against B: {show_details(another_data)}")
    selection = input("Who has more followers? Type 'A' or 'B': ").upper()
    if selection == 'A':
        results = compare(data1=first_data, data2=another_data)
    else:
        results = compare(data1=another_data, data2=first_data)

    if results == 0:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_continue = False
