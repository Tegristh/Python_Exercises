print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = 0
love = 0
message = ""
string_to_test = name1.lower() + name2.lower()
true += string_to_test.count("t")
true += string_to_test.count("r")
true += string_to_test.count("u")
true += string_to_test.count("e")
love += string_to_test.count("l")
love += string_to_test.count("o")
love += string_to_test.count("v")
love += string_to_test.count("e")
result = true * 10 + love

if result < 10 or result > 90:
	message = ", you go together like coke and mentos"

if result >= 40 and result <= 50:
	message = ", you are alright together"

print(f"Your score is {result}{message}.")