# list.append(x) - Добвыляет элкмент в конец списка
# list.extend(L) - расширает список лист, добавляя в конец все эдементы списка Д
# list.insert(i, x) - Вставляет на первый элемент значение Х
# list.remove(x) - Удаляет первый элемент в списке, имнющий значение Х. ValueError, если такого элемента не сушествует
# list.pop([i]) - Удалякт i-ый элемент и возращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) - Возращает полоэение первого элемента со значением х (при этом посик ведется от старт до энд)
# list.count(x) - Возвращает количество элементов со значением Х
# list.sort([key=], [reverse=False]) - Сортирует список на основе функции
# list.reverse() - Разворачивает список
# list.copy() - Возращает копию списка
# list.clear() - Очищает список


l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Ivanov', 'Petrov', 'Sidorov']

# print(l[4][0])
# print(l[:3])
l[2] = 'world'
# l[:2] = [10, 15]

l.append('new')
l.extend(names)
l2 = ['hi', 19]
l += l2
l.insert(1, 'test_insert')
# l.remove('world')
# el = l.pop(1)
# el_index = l.index('hello')
# print(el_index)
# print(l, l.count('world'))

l3 = ['hello', 'hi', 'David', 'world', 'test']
l3.sort()
# l3 = sorted(l3)
l3.reverse()
test = l3.copy()
test.clear()
print(l3, test, sep='\n')
