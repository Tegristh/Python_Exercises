print("Welcome to the tip calculator.")

bill = float(input("what was the total bill? $"))
percentage = input("What percentage tip would you like to give? 10,12, or 15? ")
people_number = int(input("how many people to split the bill?"))

tip = 1+ (int(percentage)/100)
total_bill = bill * tip
result = total_bill / people_number

print(f"Each person should pay: ${round(result,2)}")