"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

"""
Эффективнее всего оказался способ с гномьей сортировкой

"""

"""
Замеры(10, 100, 1000 элементов): 0.5193086, 4.9238102999999995, 137.62544259999999
"""
from statistics import median
from random import randint
from timeit import timeit

m = int(input('Число: '))
array = [randint(0, 100) for _ in range(2 * m + 1)]
print(timeit("median(array)", globals=globals()))