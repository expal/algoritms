"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def deco_time(func):
    def wrapper():
        start_val = time.time()
        r = func()
        end_val = time.time()
        return r, f'Время затраченное на выполнение {end_val - start_val}'

    return wrapper()


"""
A) Разница во времени есть, операция по заполнению списка занимает примерно 0.005 секунд, а словаря 0.0069,
 связано это с тем что словарь при заполнение использует хэши
"""


@deco_time
def func_lst():
    lst = []
    for i in range(100000):
        lst.append(i)  # сложность O(1)


print(func_lst)


@deco_time
def func_dct():
    dct = {}
    for i in range(100000):
        dct[i] = i  # сложность O(1)


print(func_dct)

"""
 B) Разница во времени есть, операция по получению элемента у списка занимает примерно 0.01, а у словаря 0.003, обе операции имеют сложность O(1)
"""


@deco_time
def func_lst_1():
    lst = [i for i in range(100000)]
    for i in range(100000):
        a = lst[i]  # сложность O(1)


print(func_lst_1)


@deco_time
def func_dct_1():
    dct = {}
    for i in range(100000):
        dct[i] = i

    for i in range(100000):
        a = dct[i]  # сложность O(1)


print(func_dct_1)

"""
C) Разница во времени есть, операция по удалению элемента у списка занимает примерно 0.8, а у словаря 0.011, связано с тем что сложность удаления у списка O(n),
а у словаря O(1)
"""


@deco_time
def func_lst_2():
    lst = [i for i in range(100000)]
    for i in range(100000):
        lst.remove(i)  # сложность O(n)


print(func_lst_2)


@deco_time
def func_dct_2():
    dct = {}
    for i in range(100000):
        dct[i] = i

    for i in range(100000):
        dct.pop(i)  # сложность O(1)


print(func_dct_2)
