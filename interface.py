# Этот модуль отвечает за вывод списка задач и прогресса
import json
from colorama import Fore, Style, init


# Эта функция получает список задач из json файла
def get_tasks(db_file):
    # В первой строчке мы прописываем из какого файла будем получать информацию
    # (db_file), затем в каком режиме ('rb' - только для чтения, побитого)
    # и записываем это в переменную file для дальнейшей работы с этим файлом.
    # Во второй строчке мы записываем в словарь tasks данные из json файла
    with open(db_file, 'rb') as file:
        tasks = json.loads(file.read().decode(encoding='utf-8', errors='replace'))
    return tasks


# Эта функция выводит список задач
def tasks_list(check_list):
    print('________________________________________________________________')
    #tasks = get_tasks(db_file)
    tasks = check_list.tasks

    print(check_list.title)
    # Выводим в консоль список задач
    for i in range(len(tasks)):
        print(tasks[i])
        for j in range(len(tasks[i].sub_tasks)):
            print(f'    {i+1}.{tasks[i].sub_tasks[j]}')


    # Выводим прогресс в процентах с двумя знаками после запятой
    progress = get_progress(check_list)
    print(f'Ваш прогресс: {round(progress, 2)}%')

    # Выводим прогресс-бар в виде символов "*"
    print('{' + '*' * int(progress) + ' ' * (100 - int(progress)) + '}')
    print('________________________________________________________________')


# Рассчитываем прогресс выполнения задач
def get_progress(check_list):
    # tasks = get_tasks(db_file)
    tasks = check_list.tasks
    progress = 0

    # Проходимся по всем задачам в чек-листе, проверяя, выполнены ли они.
    # И если выполнены, то добавляем единицу в счетчик прогресса.
    for task in tasks:
        if task.state == True:
            progress += 1

    # Если задач нет, то выводим нулевой прогресс
    if len(tasks) == 0:
        progress_percent = 0
        return progress_percent
    # Приводим вид счетчика прогресса к процентам
    progress_percent = (progress / len(tasks) * 100)
    return progress_percent