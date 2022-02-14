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
        start_val = time.perf_counter_ns()
        r = func()
        end_val = time.perf_counter_ns()
        return r, f'Время затраченное на выполнение(в наносекундах) {end_val - start_val}'

    return wrapper()

"""
A) Разницы во времени нет, в обоих случаях операция занимает 100 наносекунд, 
скорее всего это связано с тем что обе операции имеют сложность O(1)
"""
@deco_time
def func_lst():
    lst = []
    lst.append(1)  # одна операция заполнения = 100 наносекундам, сложность O(1)
    return lst


print(func_lst)


@deco_time
def func_dct():
    dct = {}
    dct[1] = '1'  # одна операция заполнения = 100 наносекундам, сложность O(1)
    return dct


print(func_dct)


# B) Разницы во времени опять нет, операции также занимают 100 наносекунд и имеют сложность O(1)
@deco_time
def func_lst_1():
    lst = [1]
    return lst[0]  # одна операция получения элемента = 100 наносекундам, сложность O(1)


print(func_lst_1)


@deco_time
def func_dct_1():
    dct = {1: '1'}
    return dct[1]  # одна операция получения элемента = 100 наносекундам, сложность O(1)


print(func_dct_1)

"""
C) В случае удаления элементов разница во времени уже присутсвует, по-скольку сложность удаления у списка O(n), 
а у словаря O(1)
"""

@deco_time
def func_lst_2():
    lst = [1, 2, 3]
    return lst.pop(0)  # одна операция удаления элемента равна примерно 200 наносекундам, сложность O(N)


print(func_lst_2)


@deco_time
def func_dct_2():
    dct = {1: '1', 2: '2', 3: '3'}
    return dct.pop(1)  # одна операция удаления элемента = 100 наносекундам, сложность O(1)


print(func_dct_2)
