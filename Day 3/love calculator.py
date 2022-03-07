print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n').lower()
name2 = input('What is their name? \n').lower()

name = name1 + name2
total_true = name.count('t') + name.count('r') + name.count('u') + name.count('e')
total_love = name.count('l') + name.count('o') + name.count('v') + name.count('e')
total = int(str(total_true) + str(total_love))

if (total < 10) or (total > 90):
    print(f'Your score is {total}, you go together like coke and mentos.')
elif (total >= 40) and (total <= 50) :
    print(f'Your score is {total}, you are alright together :)')
else:
    print(f'Your Score is {total}.')