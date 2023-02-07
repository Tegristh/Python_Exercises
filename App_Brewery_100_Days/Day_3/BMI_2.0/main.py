height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight) /(float(height)**2)
if bmi < 18.5:
	message = "you are underweight"
elif bmi < 25:
	message = "you have a normal weight"
elif bmi < 30:
	message = "you are slightly overweight"
elif bmi > 35:
	message = "you are obese"
else:
	message = "you are clinically obese"

print(f"Your BMI is {int(round(bmi,0))}, {message}.")