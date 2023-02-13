# from replit import clear 
from art import logo
# Calculator

# Add


def add(n1, n2):
    return n1 + n2

# substract


def substract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    new_cycle = True
    while new_cycle:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        num1 = answer
        if result != "y":
            # clear()
            calculator()


calculator()
