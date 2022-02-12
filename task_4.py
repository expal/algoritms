"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def func(i, num, el_count, summ):
    if i == el_count:
        return f'Сумма элементов {summ}'
    elif i < el_count:
        return func(i + 1, num / -2, el_count, summ + num)


print(func(0, 1, 3, 0))

