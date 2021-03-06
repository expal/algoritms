"""
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


def func_1(lst_obj):
    min_num = lst_obj[0]  # O(1) - константная

    for i in range(len(lst_obj)):  # O(n) - линейная
        if lst_obj[i] < lst_obj[0]:  # O(n) - линейная
            min_num = lst_obj[i]  # O(1) - константная
    return min_num  # O(1) - константная


print(func_1([3, 2, 5, 1, 4, 7, 10]))


def func_2(lst_obj):
    min_num = set(lst_obj)  # O(len()) - линейная
    return min_num.pop()  # O(1) - константная


print(func_2([3, 2, 5, 1, 4, 7, 10, 0]))
