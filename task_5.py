"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Stack:
    def __init__(self):
        self.stack_plates = [[]]

    def empty(self):
        return self.stack_plates == []

    def push(self, item):
        self.stack_plates[-1].append(item)
        if len(self.stack_plates[-1]) > 10:
            self.stack_plates.append([])

    def pop(self):
        return self.stack_plates.pop()

    def get_val(self):
        return self.stack_plates[len(self.stack_plates) - 1]

    def size(self):
        return len(self.stack_plates)


if __name__ == '__main__':
    Stack_obj = Stack()
    print(Stack_obj.size())




























