# I used Repl.it coding environnement for this program 
# from replit import clear
from art import logo
auctions = {}


def add_auction():
    name = input("what is your name?: ")
    price = int(input("what is your bid price?: $"))
    auctions[name] = price


def search_winner(dict):
    user = ""
    bid = 0
    for key in dict:
        if dict[key] > bid:
            user = key
            bid = dict[key]
    print(f"{user} wins the auction with the bid price of {bid}")


# program start:
print(logo)
other_user = True
while other_user:
    add_auction()
    result = input("Any other user? 'yes' or 'no'? \n")
    #clear()
    if result == "no":
        other_user = False
# print(auctions)
search_winner(auctions)
