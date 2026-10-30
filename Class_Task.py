# Объявляем датакласс, в котором инициализируем основные свойства задачи:
# порядковый номер, описание и состояние


class CheckList:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        for i in task:
            self.tasks.append(i)

    def __str__(self):
        output = ''
        for i in range(len(self.tasks)):
            output += f'{self.tasks[i].serial_numb}. {self.tasks[i].description} - {self.tasks[i].state}'

        return output


class Task:
    def __init__(self, serial_numb, description, state):
        self.serial_numb = serial_numb
        self.description = description
        self.state = state

    def set_serial_numb(self, serial_numb):
        if serial_numb > 0:
            self.serial_numb = serial_numb

# Объявляем класс для подзадач
class SubTask(Task):
    def __init__(self, serial_numb, description, state):
        super().__init__(serial_numb, description, state)

    # Этот метод определяет что будет выводиться при вызове класса,
    # например, через print(main_task)
    def __str__(self):
        output = f'    {self.serial_numb}. {self.description} - {self.state}'
        return output

# Объявляем класс для главных задач, в которых также может храниться список подзадач
class MainTask(Task):
    def __init__(self, serial_numb, description, state):
        super().__init__(serial_numb, description, state)
        self.sub_tasks = []

    # Этот метод позволяет добавлять подзадачи в список подзадач главной задачи
    def add_sub_tasks(self, sub_task):
        for i in sub_task:
            self.sub_tasks.append(i)

    # Этот метод определяет что будет выводиться при вызове класса,
    # например, через print(main_task)
    def __str__(self):
        output = f'{self.serial_numb}. {self.description} - {self.state}'
        return output

    def __len__(self):
        return len(self.sub_tasks)