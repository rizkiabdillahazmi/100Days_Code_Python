height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = weight / height**2
bmi_condition = ""

if bmi < 18.5:
    bmi_condition = "are underweight"
elif bmi < 25:
    bmi_condition = "have normal weight"
elif bmi < 30:
    bmi_condition = "are overweight"
elif bmi < 35:
    bmi_condition = "are obese"
else:
    bmi_condition = "are clinically obese"

print(f"Your BMI is {int(bmi)}, you {bmi_condition}")
