"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

"""
Замеры(10, 100, 1000 элементов): 0.4403073000000002, 5.364327, 153.650283
"""

from random import randint
from timeit import timeit


def median(array):
    len_array = len(array)
    index = len_array // 2
    if len_array % 2:
        return sorted(array)[index]
    return sum(sorted(array)[index - 1:index + 1]) / 2


m = int(input('Число: '))
a = [randint(-100, 100) for _ in range(2 * m + 1)]

print(timeit("median(a)", globals=globals()))
