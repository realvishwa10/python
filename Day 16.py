# Coffee machine using OOP

from menu import Menu, MenuItem
from coffee_machine import CoffeeMaker
from money_machine import MoneyMachine

machine = 'on'
menu = Menu()
cafe_machine = CoffeeMaker()
cash_register = MoneyMachine()

while machine == 'on':
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'report':
        print(cafe_machine.report())
    if order == 'off':
        print('Machine is shutting down')
        machine = 'off'
    else:
        drink = menu.find_drink(order_name=order)
        if cafe_machine.is_resource_sufficient(drink) and cash_register.make_payment(drink.cost):
            cafe_machine.make_coffee(drink)


