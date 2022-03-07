# To calculate the Body Mass Index (BMI)
weight = float(input('What is your body weight in kg? '))
height = float(input('What is your body height in m? '))

bmi = round(weight/height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")