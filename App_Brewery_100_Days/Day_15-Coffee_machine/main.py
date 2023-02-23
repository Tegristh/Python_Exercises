from data import MENU, resources


machine_on = True


def report_print(machine):
    """ create a report of ressources inside the machine"""
    print(f"Water: {machine['water']}ml")
    print(f"Milk: {machine['milk']}ml")
    print(f"Coffee: {machine['coffee']}g")
    print(f"money: ${machine['money']}")


# TODO: 2. Check resources sufficient to make drink order.


def has_materials(command):
    """ return True if materials are sufficient, or a personalised error message"""
    command_water = MENU[command]['ingredients']['water']
    command_milk = MENU[command]['ingredients']['milk']
    command_coffee = MENU[command]['ingredients']['coffee']
    machine_water = resources['water']
    machine_milk = resources['milk']
    machine_coffee = resources['coffee']
    if command_water > machine_water:
        print("Sorry there is not enough water")
        return False
    elif command_milk > machine_milk:
        print("sorry there is not enough milk")
        return False
    elif command_coffee > machine_coffee:
        print("sorry there is not enough coffee")
        return False
    else:
        return True

# TODO: 1. get the user command.


def get_user_command():
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == "report":
        print(report_print(resources))
    elif command == "off":
        quit()
        # turn off the machine
    elif command not in MENU:
        return
    else:
        return command

# TODO: 5. Process coin.


def make_coffee(command):
    """ return True if materials are sufficient, or a personalised error message"""
    command_water = MENU[command]['ingredients']['water']
    command_milk = MENU[command]['ingredients']['milk']
    command_coffee = MENU[command]['ingredients']['coffee']
    resources['water'] -= command_water
    resources['milk'] -= command_milk
    resources['coffee'] -= command_coffee


def get_money(value):
    resources['money'] += value


def process_coin(item):
    item_value = MENU[item]['cost']
    print(f"Your command cost: $ {item_value}")
    nb_quarters = int(input("how many quarters?: "))
    nb_dimes = int(input("how many dimes?: "))
    nb_nickles = int(input("how many nickles?: "))
    nb_pennies = int(input("how many pennies?: "))
    payed = round((nb_quarters*0.25)+(nb_dimes*0.1)+(nb_nickles*0.05)+(nb_pennies*0.01),2)
    if payed < item_value:
        print("Sorry that's not enough money. Money refunded")
        return False
    if payed == item_value:
        return True
    else:
        print(f"Here is ${round((payed - item_value),2)} dollars in change")
        return True


def coffee_machine():
    while machine_on:
        user_command = get_user_command()
        if (user_command in MENU) and (has_materials(user_command)):
            item_value = MENU[user_command]['cost']
            work = process_coin(user_command)
            if work:
                make_coffee(user_command)
                get_money(item_value)
                print(f"Here is your {user_command} ☕. Enjoy!")


coffee_machine()
