"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile

"""
Проблема: Из-за постоянного вызова фукнции рекурсией, постоянно появляется одна и та же таблица
Решение: Обернуть функцию доп. функцией
"""


# Проблемный вариант
@profile
def func(a, lst_obj=[]):
    reverse_num = ''.join(lst_obj)
    if a == 0:
        return reverse_num
    else:
        current_a = a % 10
        a = a // 10
        lst_obj.append(str(current_a))
    return func(a, lst_obj)


# print(func(1230))


# Решенный вариант

@profile
def wrapper(b):
    def func_1(a, lst_obj=[]):
        reverse_num = ''.join(lst_obj)
        if a == 0:
            return reverse_num
        else:
            current_a = a % 10
            a = a // 10
            lst_obj.append(str(current_a))
            return func_1(a, lst_obj)

    return func_1(b)


print(wrapper(1230))
