l = [
    1,
    2,
    3,
    'hello',
    ['test', 10],
    'world',
    True
]

# l2 = list('list')
# l3 = list((1, 2, 3))
#
# l4 = [i for i in 'hello']
# # l5 = [i for i in 'hello world' if i not in [' '] and i not in 'e']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', ' ']]
#
# print(l, l2, l3, l4, l5, sep='\n')

# range - генератор, не возращает последовотельность, генератор

# l6 = list(range(1, 10, 2))
# print(l6)

for i in range(1, 3):
    print(f'Outside cycle #{i}')
    for j in range(1, 3):
        print(f'\t Inner cycle #{j}')
