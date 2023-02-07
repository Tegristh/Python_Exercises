rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choices = [rock, paper, scissors]
user = int(input("What do you choose? \n type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)
if user == computer:
  message = "It's a Draw"
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
  message = "You win"
else:
  message = "You loose"

print(choices[user])
print("Computer chose:")
print(choices[computer])
print(message)