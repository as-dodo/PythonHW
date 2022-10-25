#
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
#
# from math import sqrt
#
# def square(side):
#     per = 4 * side
#     sq = side ** 2
#     diag = round(side * sqrt(2))
#     # diag = round(side * 2 ** 0.5)
#     return per, sq, diag
#
#
# print(square(5))

#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def print_info(**kwargs):

    # for x in kwargs:
    #     print(f'{x}: {kwargs[x]}')

    # info = list(map(lambda x: print(f'{x}: {kwargs[x]}'), kwargs))
    # return info

#
# print_info(name='John', last_name='Smith', age=35, position='web developer')

#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

new_list = [20, -3, 15, 2, -1, -21]

# print(list(filter(lambda x: x > 0, new_list)))

#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, new_list))

#
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

from my_calc import *
#
# print(sum_it(5, 5))
# print(diff_it(5, 5))
# print(multi(5, 5))
# print(div(5, 0))

# def tests():
#     assert sum_it(3, 3) == 6, 'Wrong number'
#     assert diff_it(5, 3) == 2, 'Wrong number'
#     assert multi(3, 3) == 9, 'Wrong number'
#     assert div(4, 4) == 1, 'Wrong number'
#
# tests()

