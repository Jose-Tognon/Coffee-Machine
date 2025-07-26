from coffee_maker import CofeeMaker
from money_machine import MoneyMachine
from menu import Menu,MenuItem

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CofeeMaker()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}):')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink):
            coffee_maker.make_coffee(drink)

