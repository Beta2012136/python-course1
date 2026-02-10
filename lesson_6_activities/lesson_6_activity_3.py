height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height / 100) ** 2
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are normal weight")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.9:
    print("You are obese")
elif bmi <= 39.9:
    print("You are too obese McDonals and KFC are your mortal enimeis now")
else:
    print("You are morbidly obese you should see a doctor immediately")