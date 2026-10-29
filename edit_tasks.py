# Этот модуль отвечает за редактирование списка задач
import json

#
from interface import tasks_list, get_tasks


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
        tasks.update({new_task_id: {task: False}})

        # Условный оператор для выхода из цикла, если пользователь
        # ввел один из символов в списке symbol_list
        if input('Вы хотите добавить еще одну задачу? (д/н) ') in symbol_list:
            adding_task = False

    save_in_json(tasks, db_file)
    return tasks


# Эта функция завершает выполнение задачи в чек-листе
def complete_tasks(db_file):
    tasks_list(db_file)
    tasks = get_tasks(db_file)
    get_complete = ''

    # Цикл, который требует от пользователя ввести номер задачи для ее завершения
    while get_complete not in tasks.keys():
        get_complete = input('Введите номер задачи,'
                            ' которую вы завершили (0 - для отмены): ')
        if get_complete == '0':
            return tasks

    # По полученному номеру задачи получаем наименование задачи и ее статус.
    # Меняем статус задачи на True - выполнена
    for k in tasks[str(get_complete)].keys():
        tasks[str(get_complete)][k] = True

    save_in_json(tasks, db_file)
    return tasks


# Эта функция удаляет задачи из чек-листа
def delete_tasks(db_file):
    tasks_list(db_file)
    tasks = get_tasks(db_file)
    task_id = ''

    # Цикл, который требует от пользователя ввести номер задачи для удаления
    while task_id not in tasks.keys():
        task_id = input('Введите номер задачи,'
                        ' которую хотите удалить (0 - для отмены): ')
        if task_id == '0':
            return tasks

    # Если задача, введенная пользователем последняя в списке,
    # то мы просто удаляем ее, не заходя в цикл перезаписи.
    # Иначе:
    # Проходимся по всем задачам после той, которую нужно удалить.
    # Перезаписываем все задачи после удаленной, чтобы они поднялись по порядковому номеру
    if int(task_id) == len(tasks.keys()):
        del (tasks[str(task_id)])
        print(f'Задача №{task_id} успешно удалена')
    else:
        for k in range(int(task_id), len(tasks.keys())):
            tasks[str(k)] = tasks.pop(str(k + 1))
        print(f'Задача №{task_id} успешно удалена')

    save_in_json(tasks, db_file)
    return tasks