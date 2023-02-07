import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_player = len(names)
victim = random.randint(0,number_of_player-1)
victim_name = names[victim]

print(f"{victim_name} is going to buy the meal today!")