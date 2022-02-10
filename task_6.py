"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.current_queue = QueueClass()
        self.rework_queue = QueueClass()
        self.solved_tasks = []

    def solved_task(self):
        task = self.current_queue.from_queue()
        self.solved_tasks.append(task)

    def revision_task(self):
        task = self.current_queue.from_queue()
        self.rework_queue.to_queue(task)

    def to_current_queue(self, item):
        self.current_queue.to_queue(item)

    def from_revision(self):
        task = self.rework_queue.from_queue()
        self.current_queue.to_queue(task)

    def current_task(self):
        return self.current_queue.elems[len(self.current_queue.elems) - 1]

    def current_revision(self):
        return self.rework_queue.elems[len(self.rework_queue.elems) - 1]

    def solved_tasks(self):
        return self.solved_tasks
