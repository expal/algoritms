"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

"""
    Вывод: 
    Первое решение лучше, по-скольку использует обычную сортировку и имеет сложность O(N log N), а
    второе решение использует пузырьковую сортировку, что является одной из худшей сортировкой и имеет сложность O(n^2)

"""


def func_1(dict_obj):  # Общая сложность: O(N log N)
    list_obj = []  # O(len()) - линейная
    for keys, value in dict_obj.items():  # O(n) - линейная
        list_obj.append(value)  # O(1) - константная
        list_obj.sort()  # O(N log N) - логарифмическая
        list_obj.reverse()  # O(n) - линейная
    return list_obj[0:3]  # O(1) - константная


print(func_1({'Company1': 140000,
              'Company2': 170000,
              'Company3': 100000,
              'Company4': 50000,
              'Company5': 20000000,
              'Company6': 80000,
              'Company7': 150000}))


def func_2(dict_obj):  # Общая сложность: O(n^2)
    swapped = True  # O(1) - константная
    list_obj = []  # O(len()) - линейная
    for keys, value in dict_obj.items():  # O(n) - линейная
        list_obj.append(value)  # O(1) - константная

    while swapped:  # O(n) - линейная
        swapped = False  # O(1) - константная
        for i in range(len(list_obj) - 1):  # O(len()) - линейная
            if list_obj[i] > list_obj[i + 1]:  # O(n) - линейная
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]  # O(1) - константная
                swapped = True  # O(1) - константная
    return list_obj[-3:]  # O(1) - константная


print(func_2({'Company1': 140000,
              'Company2': 170000,
              'Company3': 100000,
              'Company4': 50000,
              'Company5': 20000000,
              'Company6': 80000,
              'Company7': 150000}))
