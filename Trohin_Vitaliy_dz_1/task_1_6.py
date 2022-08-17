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
        self.basic = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.basic == []

    def to_queue(self, item):
        self.basic.insert(0, item)

    def from_queue(self):
        return self.basic.pop()

    def to_solved(self):
        self.solved.insert(0, self.basic.pop())

    def to_revision(self):
        self.revision.insert(0, self.basic.pop())

    def solved_problems(self):
        self.basic.insert(0, self.revision.pop())

    def size(self):
        return len(self.basic)


if __name__ == '__main__':
    qc_obj = QueueClass()

    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.basic)
    qc_obj.to_solved()
    print(qc_obj.solved)
    qc_obj.to_revision()
    print(qc_obj.basic)
    print(qc_obj.revision)
    qc_obj.solved_problems()
    print(qc_obj.revision)
    print(qc_obj.basic)
