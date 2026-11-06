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

    print(f'{check_list.title}\n')
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


# def print_check_list_menu(check_lists):
#     control_symbol = []
#     check_list_menu = ''
#     # Цикл для меню работы с чек-листами
#     while check_list_menu not in control_symbol:
#         # Списки символов, которые необходимо ввести
#         # для добавления или удаления чек-листа
#         symbol_for_add = ['д', 'Д', 'l', 'L']
#         symbol_for_del = ['у', 'У', 'e', 'E']
#
#         for i in range(len(check_lists)):
#             print(f'{check_lists[i].serial_numb}. {check_lists[i].title}')
#
#         print('Выберите чек лист по номеру')
#         print('Введите "д" чтобы добавить чек лист')
#         print('Введите "у" чтобы удалить чек лист')
#         print('Введите 0 для выхода из программы')
#         check_list_menu = input()
#
#         if check_list_menu in control_symbol:
#             check_list = check_lists[int(check_list_menu) - 1]
#             return check_list
#
#         elif check_list_menu in symbol_for_add:
#             adding_check_list(check_lists)
#
#         elif check_list_menu in symbol_for_del:
#             check_lists = delete_check_list(check_lists)
#
#         elif check_list_menu != '0':
#             print(Fore.RED + 'Ввод некорректен!')
#
#         if check_list_menu == '0':
#             return 0