"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import collections
import timeit

"""
Вывод: у OrderedDict очень большое различие во времени, мне кажется что его нет смысла использовать в Python 3.6 и 
более поздних версиях, только если очень важен порядок словаря
"""


# заполнение словаря
def dct_filling():
    dct = dict(zip(range(100), [x for x in range(100)]))


print(timeit.timeit("dct_filling()", globals=globals()))  # 5.5910034


def order_dct_filling():
    dct = collections.OrderedDict(zip(range(100), [x for x in range(100)]))  # 10.8034862


print(timeit.timeit("order_dct_filling()", globals=globals()))


# получение ключ: значение

def dct_items():
    dct = dict(zip(range(100), [x for x in range(100)]))
    for key, value in dct.items():
        pass


print(timeit.timeit("dct_items()", globals=globals()))  # 6.997995899999999


def order_dct_items():
    dct = collections.OrderedDict(zip(range(100), [x for x in range(100)]))
    for key, value in dct.items():
        pass


print(timeit.timeit("order_dct_items()", globals=globals()))  # 14.062489599999996
