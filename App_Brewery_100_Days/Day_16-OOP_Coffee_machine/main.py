from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_menu = Menu()
machine_on = True

while machine_on:
    user_command = input(
        f"What would you like? ({machine_menu.get_items()}): ")
    if user_command == "report":
        coffee_machine.report()
        money_machine.report()
    elif user_command == "off":
        machine_on = False
    else:
        order = machine_menu.find_drink(user_command)
        if coffee_machine.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_machine.make_coffee(order)
