# Этот модуль отвечает за редактирование списка задач
import json

#
from interface import tasks_list, get_tasks
from Class_Task import MainTask, SubTask, CheckList

# Функция для сохранения чек-листа в файле json
def save_in_json(tasks, db_file):
    with open(db_file, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


# Эта функция добавляет задачи в чек-лист
def adding_tasks(tasks, db_file):
    symbol_list = ['н', 'Н', 'y', 'Y', 'нет', 'Нет', 'no', 'No']
    adding_task = True  # Переменная для выхода из цикла

    # Цикл для добавления нескольких задач
    while adding_task == True:
        new_task_id = len(tasks) + 1
        task = input('Введите имя задачи (0 - для отмены): ')

        if task == '0':
            return tasks

        # Добавляем в конец чек-листа новую задачу
        # и присваиваем ей статус False - не выполнена
        tasks.append(MainTask(new_task_id, task, False))

        # Условный оператор для выхода из цикла, если пользователь
        # ввел один из символов в списке symbol_list
        if input('Вы хотите добавить еще одну задачу? (д/н) ') in symbol_list:
            adding_task = False

    # save_in_json(tasks, db_file)
    return tasks


# Эта функция завершает выполнение задачи в чек-листе
def complete_tasks(tasks):
    # tasks_list(db_file)
    # tasks = get_tasks(db_file)
    get_complete = -1

    # Цикл, который требует от пользователя ввести номер задачи для ее завершения
    while 0 >= get_complete or get_complete > len(tasks):
        try:
            get_complete = int(input('Введите номер задачи,'
                                     ' которую вы завершили (0 - для отмены): '))
            if get_complete == '0':
                return tasks
        except ValueError:
            get_complete = -1
            print('Нужно ввести целое число!')
    # По полученному номеру задачи получаем наименование задачи и ее статус.
    # Меняем статус задачи на True - выполнена
    tasks[get_complete - 1].state = True

    # save_in_json(tasks, db_file)
    return tasks


# Эта функция удаляет задачи из чек-листа
def delete_tasks(tasks):
    # tasks_list(db_file)
    # tasks = get_tasks(db_file)
    task_id = -1

    # Цикл, который требует от пользователя ввести номер задачи для удаления
    while 0 >= task_id or task_id > len(tasks):
        try:
            task_id = int(
                input('Введите номер задачи,'
                      ' которую хотите удалить (0 - для отмены): '))
            if task_id > len(tasks):
                print('Задачи с таким номером не существует!')
            elif task_id == 0:
                return tasks
        except ValueError:
            task_id = -1
            print('Нужно ввести целое число!')

    # Если задача, введенная пользователем последняя в списке,
    # то мы просто удаляем ее, не заходя в цикл перезаписи.
    # Иначе:
    # Проходимся по всем задачам после той, которую нужно удалить.
    # Перезаписываем все задачи после удаленной, чтобы они поднялись по порядковому номеру
    if task_id == len(tasks):
        del (tasks[task_id - 1])
        print(f'Задача №{task_id} успешно удалена')
    else:
        for k in range(task_id - 1,
                       len(tasks) - 1):
            tasks[k] = tasks[k + 1]
            tasks[k].serial_numb -= 1
        tasks.pop()
        print(f'Задача №{task_id} успешно удалена')

    # save_in_json(tasks, db_file)
    return tasks