# dict.clear() - очищает словарь
# dict.copy() - возращает копию словаря
# dict.get(key [, default]) - ворзращает значение ключа, если его нету,
# dict.items() - возращает пары, ключ значение
# dict.keys() - возращает ключи в словаре
# dict.pop(key [, default]) - удаляет ключ и возращает значение, если ключа нет -  default
# dict.popitem() - удаляет и возращает пары, ключ значение, если словарь пуст, бросает KeyErrors
# dict.setdefault() - ворзращает значение ключа, если его нету, то создаст default: None в конце словаря
# dict.update(other) - добавляет пару ключ значение из other
# dict.values() - возвращает значение а словаре

product1 = {
    'title': 'Sony',
    'price': 100
}

# print(product1.items())
# print(product1.keys())
# print(product1.pop('title'))
# print(product1.pop('title2', 'NO!!!!'))
# print(product1.popitem())

print(product1)
# print(product1.setdefault('title'))
product1.update({'test': 'value'})
product1.update({'price': 1000})
print(product1)
print(product1.values())
