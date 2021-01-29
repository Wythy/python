my_str = ['А роза упала на лапу Азора', 'Около Миши молоко', 'askjdhksfhjkas', 'Около Миши молоко']
test = []

for i in my_str:
    i_r = i.replace(' ', '').lower()
    if i_r == i_r[::-1]:
        test.append(i)
    # if i != i[::-1]:
    #     continue

print(test)