import random

secret_number = random.randint(1, 5)
user_number = input('Please enter your number in range of 1 to 5: ')

if user_number.isdigit():
    user_number = int(user_number)
else:
    print('You input not a number!')

if user_number > secret_number:
    print('Your number is more')

if user_number < secret_number:
    print('Your number is less')

if user_number == secret_number:
    print('Congratulation!!!, you deal one trying!')

count = 1
while user_number != secret_number:
    count += 1
    user_number = input('Please enter your number in range of 1 to 5: ')

    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('You input not a number!')

    if user_number > secret_number:
        print('Your number is biggest')

    if user_number < secret_number:
        print('Your number is light')

    if user_number == secret_number:
        print(f'Congratulation!!!, you deal {count} trying')