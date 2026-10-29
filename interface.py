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
# init(autoreset=True) включает автоматический сброс оформления текста от принта к принту
def tasks_list(db_file):
    init(autoreset=True)

    print('________________________________________________________________')
    tasks = get_tasks(db_file)

    # Проходимся по всем задачам по ключам.
    # Получаем наименование каждой задачи.
    # Проверяем статус каждой задачи, если выполнена:
    # Пишем "Выполнена", иначе: пишем "Ждет выполнения"
    for i in tasks.keys():
        for j in tasks[i].keys():
            if tasks[i][j] == True:
                print(f'{i}. {j} - '+ Fore.GREEN + 'Выполнена!')
            else:
                print(f'{i}. {j} - '+ Fore.RED + 'Ждет выполнения')

    # Выводим прогресс в процентах с двумя знаками после запятой
    print(f'Ваш прогресс: {round(get_progress(db_file), 2)}%')

    # Выводим прогресс-бар в виде символов "*"
    print('{' + '*' * int(get_progress(db_file)) + ' ' * (100 - int(get_progress(db_file))) + '}')
    print('________________________________________________________________')


# Рассчитываем прогресс выполнения задач
def get_progress(db_file):
    tasks = get_tasks(db_file)
    progress = 0

    # Проходимся по ключам словаря.
    # Проходимся по всем задачам, проверяя, выполнены ли они и если выполнены,
    # то добавляем единицу в счетчик прогресса.
    for task_id in tasks.keys():
        for k, v in tasks[task_id].items():
            if v == True:
                progress += 1

    # Приводим вид счетчика прогресса к процентам
    progress_percent = (progress / len(tasks) * 100)
    return progress_percent