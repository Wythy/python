words = ['madam', 'topot', 'test', 'madam', 'word']
my_str = ['А роза упала на лапу Азора', 'Около Миши молоко']
# words_copy = []
# words_poly = []

# 1.
# test1 = words[0]
# reversed(test1)
# print(test1)

# words[0] = words[0][::-1]
# print(words[0])

# count = 0
#
# for i in words:
#     words[count] = words[count][::-1]
#     count += 1
#

print(words)
# print(words_copy)

# words_copy = words.copy()
count = 0
for i in words:
    if words[count] == words[count][::-1]:
        # print('True')
        words[count] = words[count][::-1]
        count += 1
    elif words[count] != words[count][::-1]:
        # print("False")
        words.remove(i)
        count += 1
        # continue

print(words)
# print(words_copy)

# w_count = 0
# while w_count < len(words_copy) and len(words):
#     if words_copy[w_count] == words[w_count]:
#         status = True
#         print('PASS', end=' -> ')
#         print(status)
#     else:
#         status = False
#         print('FAILED', end=' -> ')
#         print(status)
#
#     w_count += 1
#
#
#
#
# print(words)
# print(words_copy)
# print(words_poly)