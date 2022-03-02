"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

"""
Замеры(10, 100, 1000 элементов): 0.10489550000000003, 0.10428799999999994, 0.12314150000000001
"""


def gnome_sort(array):
    i, size = 1, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array

m = int(input('Число: '))
if m > 0:
    array = [randint(0, 100) for _ in range(2 * m + 1)]
else:
    ''

def median(sorted_array=gnome_sort(array)):
    len_array = len(sorted_array)
    index = len_array // 2
    if len_array % 2:
        return sorted_array[index]
    return sum(sorted_array[index - 1:index + 1]) / 2


print(timeit("median()", globals=globals()))
