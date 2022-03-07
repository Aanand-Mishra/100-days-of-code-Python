# Program to order pizza and calculate the total cost.

print('Welcome to Python Pizza Deliveries.')
size = input('What size pizza do you want? s, m or l \n').lower()
add_pepperoni = input('Do you want to add pepperoni? y or n \n').lower()
extra_cheese = input('Do you want extra cheese? y or n \n').lower()

bill = 0

if size == 's':
    bill += 15
    if add_pepperoni == 'y':
        bill += 2
    else:
        bill
    if extra_cheese == 'y':
        bill += 1
    else:
        bill

elif size == 'm':
    bill += 20
    if add_pepperoni == 'y':
        bill += 3
    else:
        bill
    if extra_cheese == 'y':
        bill += 1
    else:
        bill

elif size == 'l':
    bill += 25
    if add_pepperoni == 'y':
        bill += 3
    else:
        bill
    if extra_cheese == 'y':
        bill += 1
    else:
        bill
else:
    print('Please provide correct input')
 
print(f'Your final bill is: ${bill}')