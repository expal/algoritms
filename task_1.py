"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from timeit import timeit
from random import randint


"""
Без доработки: 0.5516660999999999
С доработкой: 0.3041423
Доработка помогла, но эффективна она будет только в маленьких объемах данных

"""

# Изначальный вариант
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [randint(0, 100) for _ in range(1000)]
print(array)
print(bubble_sort(array))
print(timeit("bubble_sort(array[:])", globals=globals(), number=10))


# Доработанный вариант

def bubble_sort_2(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [randint(0, 100) for _ in range(1000)]
print(array)
print(bubble_sort_2(array))
print(timeit("bubble_sort_2(array[:])", globals=globals(), number=10))
