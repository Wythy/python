words = ['madam', 'topot', 'test', 'madam', 'word']
test = []
# palindromes = [i for i in words if i == i[::-1]]
# print(palindromes)

# print(words)
#
# count = 0
# for i in words:
#     if words[count] == words[count][::-1]:
#         words[count] = words[count][::-1]
#         count += 1
#     elif words[count] != words[count][::-1]:
#         words.remove(i)
#         count += 1
#
# print(words)

for i in words:
    if i == i[::-1]:
        test.append(i)
    #
    # if i != i[::-1]:
    #     continue

print(test)
