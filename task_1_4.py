"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""

""" Курс: Алгоритмы и структуры данных на Python
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

"""
Сделано: Взаместо "изобретения велосипеда" использована встроенная функция
Занимает: 0.0 MiB MiB взаместо 0.0078125 MiB
"""

from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Затраченная память {mem_diff} MiB'

    return wrapper


# Изначальный вариант
@decor
def func_1(lst_obj):
    min_num = lst_obj[0]  # O(1) - константная

    for i in range(len(lst_obj)):  # O(n) - линейная
        if lst_obj[i] < lst_obj[0]:  # O(n) - линейная
            min_num = lst_obj[i]  # O(1) - константная
    return min_num  # O(1) - константная


print(func_1([3, 2, 5, 1, 4, 7, 10]))


# Оптимизированный вариант
@decor
def func_2(lst_obj):
    return min(lst_obj)


print(func_2([3, 2, 5, 1, 4, 7, 10]))
