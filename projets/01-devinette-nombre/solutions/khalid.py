import random

random_number = random.randint(0,100)

while True:
    user_input = int(input('Propose a number between 0-100: '))
    if (user_input < random_number):
        print('Your number is lesser')
    elif (user_input > random_number):
        print('Your number is greater')
    else:
        print(f'Perfect you won the number is : {random_number}')
        break