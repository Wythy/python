import random

secret_number = random.randint(1, 5)


def input_value(count):

    user_number = input('Please enter your number in range of 1 to 5: ')

    if user_number.isdigit():
        user_number = int(user_number)
        equals_value(secret_number, user_number, count)
    else:
        count += 1
        print('You input not a number!')
        input_value(count)


def equals_value(secret_number_e, user_number, count):

    if user_number > secret_number_e:
        count += 1
        print('Your number is more')
        input_value(count)

    if user_number < secret_number_e:
        count += 1
        print('Your number is less')
        input_value(count)

    if user_number == secret_number_e:
        print(f'Congratulation!!!, you deal {count} trying')


if __name__ == '__main__':
    input_value(1)
