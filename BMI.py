#code to calculate the Body Mass Index (BMI)

weight = float(input("Please enter your weight in kg: \n"))
height = float(input("Please enter your height in m:\n"))
bmi=round(weight/height**2,2)
if bmi < 18.5:
    classification = "Underweight"
elif bmi >=18.5 and bmi < 25:
    classification = "Normal Weight"
elif bmi >=25 and bmi <= 29.9:
    classification = "Overweight"
else:
    classification = "Obese"

print(f"Your BMI is: {bmi}kg/m\u00b2 with a classification of: \"{classification}\"")