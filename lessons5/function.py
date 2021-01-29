def mul_table(s, a):

    if s == 0 or s < 0 or a == 0 or a == 1 or a < 0:
        s = 9
        a = 9

    for i in range(1, s + 1):
        for j in range(2, a + 1):
            print(f'{i} * {j} = {i * j}', end='\t')
        print()


def set_register(string):

    string = str(string)

    if ' ' in string:
        return string.upper()
    else:
        return string.lower()


if __name__ == '__main__':
    mul_table(1, 1)
    print(set_register('Hello world'))
    print(set_register('Hello,world'))