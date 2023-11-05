# Coffee machine

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

water = 300
milk = 200
coffee = 100
money = 0


# TODO: Step.1: Print all the resources of the coffee machine


def report(water_details, milk_details, coffee_details, money_details):
    print(f"Water: {water_details}ml\nMilk: {milk_details}ml\nCoffee: {coffee_details}g\nMoney: ${money_details}")
    return


# TODO: Check supply
def supply_check(water_left, milk_left, coffee_left, user_choice):
    if water_left < menu[user_choice]['ingredients']['water']:
        print("Sorry there is not enough water")
        return False
    elif user_choice in ['latte', 'cappuccino'] and milk_left < menu[user_choice]['ingredients']['milk']:
        print("Sorry there is not enough milk")
        return False
    elif coffee_left < menu[user_choice]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


# TODO: Check change


def change(quarter_count, dime_count, nickle_count, penny_count):
    quarter_value = quarter_count * 0.25
    dime_value = dime_count * 0.10
    nickle_value = nickle_count * 0.05
    penny_value = penny_count * 0.01
    total_change = quarter_value + dime_value + nickle_value + penny_value
    return total_change


machine = 'on'
while machine == 'on':
    # TODO: Step 2: Get user's order

    choice = input(" What would you like? (espresso/ latte/ cappuccino): ").lower()
    if choice == 'report':
        report(water, milk, coffee, money)
    elif choice in ['espresso', 'latte', 'cappuccino']:
        if supply_check(water, milk, coffee, choice):
            print("Please insert coins")
            num_of_quarters = int(input("how many quarters: "))
            num_of_dimes = int(input("how many dimes: "))
            num_of_nickles = int(input("how many nickles: "))
            num_of_pennies = int(input("how many pennies: "))
            customer_change = change(num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies)
            if customer_change >= menu[choice]['cost']:
                water -= menu[choice]['ingredients']['water']
                if choice in ['latte', 'cappuccino']:
                    milk -= menu[choice]['ingredients']['milk']
                coffee -= menu[choice]['ingredients']['coffee']
                money += menu[choice]['cost']
                balance = customer_change - menu[choice]['cost']
                print(f"Here is ${balance} in change")
                print(f"Here is you {choice}. Enjoy :)")
            else:
                print("Sorry that's not enough money. Money refunded")
        if water < menu['espresso']['ingredients']['water'] or coffee < menu['espresso']['ingredients']['coffee']:
            print('We ran out of supply.')
            machine = 'off'
    else:
        print("Wrong choice")

print("That's all for today")
