# 1. Дан список. Получите новый список, вкотором каждое значение будет удвоено
# 2. Дан список. Возведите в квадрат каждый из его элементов и полчить сумму всех полученных квадратов
# 3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвтжтвания и пьет 0,5 литра воды
#    в чам. Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет,
#    с округлением до наименьшего значения
# 4. Проверить еслть ли в строке пробел, если нет - то преобразовать строку к нижнему регистру, если есть к верхнему

# 1.
# li = [1, 2, 3, 'test']
#
# for i in range(0, len(li)):
#     li[i] *= 2
#
# print(li)
#
# 1.T
# l1 = [1, 2, 3]
# l2 = [i * 2 for i in l1]
# print(l2)
#

# 2.
# li = [1, 2, 3]
# count = 0
#
# for i in range(0, len(li)):
#     li[i] = li[i] ** 2
#
# for j in li:
#     count += j
# print(count)
#
# 2.T
# l1 = [1, 2, 3]
# res = 0
# for num in l1:
#     res += num ** 2
# print(res)
#

# 3.
# import math
#
# input_value = input('Whats liters of water u drink?: ')
#
# if input_value.isalpha() or input_value.isspace() or input_value == "":
#     print('U input not a number!')
#
# if input_value.lstrip("-+").isdigit():
#     if int(input_value) <= 0:
#         print('Today u not a drink!')
#
# input_value = float(input_value)
# input_value *= 0.5
# # input_value = round(input_value)
# input_value = math.floor(input_value)
# print(input_value)
#
# 3.T
# time1 = 3
# time2 = 6.7
# time3 = 11.8
#
# print(time1 // 2)
# print(time2 // 2)
# print(time3 // 2)
#
# print(int(time1 / 2))
# print(int(time2 / 2))
# print(int(time3 / 2))
#

# 4.
# s = 'Hello World'
# if ' ' in s:
#     s = s.upper().replace(' ', '_')
# else ' ' not in s:
#     s = s.lower()
#
# print(s)

