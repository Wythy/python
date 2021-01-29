from random import randint


def input_value(count, secret_number):

    user_number = input('Please, enter number in range 1 - 5: ')

    if user_number.isdigit():
        user_number = int(user_number)
        get_game_answer(secret_number, user_number, count)
    else:
        count += 1
        print('You enter not a number')
        input_value(count, secret_number)


def get_game_answer(secret_number, user_number, count):

    if secret_number == user_number:
        print(f"Congratulation! You win! And makes: {count} trying.")
        repeat_game(count, secret_number)

    if secret_number < user_number:
        louse_answer("You value is more!", count, secret_number)

    if secret_number > user_number:
        louse_answer("You value is less!", count, secret_number)


def louse_answer(answer, count, secret_number):

    count += 1
    print(answer)
    input_value(count, secret_number)


def repeat_game(count, secret_number):

    repeat_input = input("Play again?[Y/N]")

    if repeat_input == 'Y' or repeat_input == 'y':
        count = 1
        secret_number = randint(1, 5)
        input_value(count, secret_number)
    elif repeat_input == 'N' or repeat_input == 'n':
        print(f"Congratulation! You win! And makes: {count} trying.")
    else:
        repeat_game(count, secret_number)


if __name__ == "__main__":

    flag = 1
    number = randint(1, 5)
    input_value(flag, number)
