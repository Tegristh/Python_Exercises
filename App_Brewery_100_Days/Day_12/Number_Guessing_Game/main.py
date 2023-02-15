import random
from art import logo


def compare(user, computer):
    if user > computer:
        return "Less"
    else:
        return "More"


# on choisit un nombre entre 0 et 100 à faire deviner au joueur
solution = random.randint(1, 100)
life = 10
solution_found = False

print(logo)
print("Welcome to Number guess - Ultimate!")
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    life -= 5
while life > 0 and not solution_found:
    #  print(f"pssst the solution is {solution}!")
    print(f"You have {life} attempts to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess < 1 or user_guess > 100:
        user_guess = int(
            input("you have to pick a number between 1 and 100: "))
    elif user_guess == solution:
        solution_found = True
        print(f"You guessed right! the number was {solution}")
    else:
        print(compare(user=user_guess, computer=solution))
        life -= 1
        if life == 0:
            print("you've run out of guesses, you loose")
        else:
            print("Guess again")
