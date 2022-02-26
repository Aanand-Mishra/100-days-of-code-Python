# Excercise 1 - Find the sum of digits in an integer.
number = input('Enter two digit number: ')
print(int(number[0]) + int(number[1]))

# Excercise 2 - BMI Calculator
weight = input('What is your body weight in kg ? \n')
height = input('What is your body height in m? \n')
bmi = int(float(weight)/float(height)**2)
print('Your Body Mass Index(BMI) is: ' + str(bmi))

# Excercise 3 - Life in Weeks
age = input("What is your current age? \n")

daysLeft = 365*(90-(int(age)))
weeksLeft = 52*(90-(int(age)))
monthsLeft = 12*(90-(int(age)))

print(f"You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.")