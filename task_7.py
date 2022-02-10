"""
Задание 7. На закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, item):
        self.elems.append(item)

    def add_to_rear(self, item):
        self.elems.insert(0, item)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(word):
    DC_obj = DequeClass()
    new_word = word.replace(' ', '')
    for el in new_word:
        DC_obj.add_to_rear(el)

    equal = True

    while DC_obj.size() > 1 and equal:
        first = DC_obj.remove_from_front()
        last = DC_obj.remove_from_rear()
        if first != last:
            equal = False

    return equal


print(pal_checker('молоко делили ледоколом'))