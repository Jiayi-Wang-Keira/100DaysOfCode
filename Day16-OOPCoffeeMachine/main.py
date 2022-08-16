from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
should_continue = True
my_menu = Menu()

while should_continue:
    action = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if action == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    elif action == 'off':
        should_continue = False
    else:
        my_menuitem = my_menu.find_drink(action)
        if my_coffee_maker.is_resource_sufficient(my_menuitem):
            cost = my_menuitem.cost
            if my_money_machine.make_payment(cost):
                my_coffee_maker.make_coffee(my_menuitem)


