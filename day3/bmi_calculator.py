height = float(input("Enter your height in m? "))
weight = float(input("Enter your weight in kg? "))

bmi = round(weight / height ** 2)
var = None
if bmi < 18.5:
    var = "underweight"
elif 18.5 <= bmi < 25:
    var = "normal weight"
elif 25 <= bmi < 30:
    var = "overweight"
elif 30 <= bmi < 35:
    var = "obese"
else:
    var = "clinically obese"

print(f"your BMI is {bmi}, you are slightly {var}")
