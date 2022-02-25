"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

import collections
import timeit


# 1)

# A) Вывод: Операция append с деком быстрее чем со списком на 0.6 сек
def list_append():
    lst = []
    for i in range(100):
        lst.append(i)


print(timeit.timeit("list_append()", globals=globals()))  # 3.8155001000000004


def deque_append():
    deque = collections.deque()
    for i in range(100):
        deque.append(i)


print(timeit.timeit("deque_append()", globals=globals()))  # 3.2645358


# B) Вывод: Операция pop с деком быстрее чем со списком на 0.6 сек
def list_pop():
    lst = [i for i in range(100)]
    for i in range(100):
        lst.pop()


print(timeit.timeit("list_pop()", globals=globals()))  # 5.7454979999999995


def deque_pop():
    deque = collections.deque([i for i in range(100)])
    for i in range(100):
        deque.pop()


print(timeit.timeit("deque_pop()", globals=globals()))  # 5.176724700000001


# C) Вывод: Операция extend с деком медлнее чем со списком на 1.3 сек
def list_extend():
    lst = []
    for i in range(100):
        lst.extend([i])


print(timeit.timeit("list_extend()", globals=globals()))  # 5.589465799999999


def deque_extend():
    deque = collections.deque()
    for i in range(100):
        deque.extend([i])


print(timeit.timeit("deque_extend()", globals=globals()))  # 6.853955800000001


# 2)

# A) Вывод: Операция append_left с деком быстрее чем со списком на 0.7 сек
def list_append_left():
    lst = []
    for i in range(100):
        lst.append(i)


print(timeit.timeit("list_append_left()", globals=globals()))  # 3.8544201


def deque_append_left():
    deque = collections.deque()
    for i in range(100):
        deque.appendleft(i)


print(timeit.timeit("deque_append_left()", globals=globals()))  # 3.200440200000001


# B) Вывод: Операция pop_left с деком быстрее чем со списком на 0.6 сек
def list_pop_left():
    lst = [i for i in range(100)]
    for i in range(100):
        lst.pop()


print(timeit.timeit("list_pop_left()", globals=globals()))  # 5.7647852


def deque_pop_left():
    deque = collections.deque([i for i in range(100)])
    for i in range(100):
        deque.popleft()


print(timeit.timeit("deque_pop_left()", globals=globals()))  # 5.1882281

# C) Вывод: Операция extended_left с деком медленее чем со списком на 1.2 сек
def list_extended_left():
    lst = []
    for i in range(100):
        lst.extend([i])


print(timeit.timeit("list_extended_left()", globals=globals()))  # 5.5399512999999985


def deque_extended_left():
    deque = collections.deque()
    for i in range(100):
        deque.extendleft([i])


print(timeit.timeit("deque_extended_left()", globals=globals()))  # 6.7205169

#
# 3) Вывод: Операция получения элемента с деком медленее чем со списком на 1 сек
def list_index():
    lst = [i for i in range(100)]
    for i in range(100):
        lst[i]


print(timeit.timeit("list_index()", globals=globals()))  # 3.9332485999999998


def deque_index():
    deque = collections.deque([i for i in range(100)])
    for i in range(100):
        deque[i]


print(timeit.timeit("deque_index()", globals=globals()))  # 4.972834300000001
