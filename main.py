# Этот модуль отвечает за запуск приложения и работу меню

from colorama import Fore, init

# Импортируем функции из других файлов
from edit_tasks import adding_tasks, complete_tasks, delete_tasks
from interface import tasks_list, get_tasks


def main ():
    # Объявляем словарь с тестовыми данными
    # init (autoreset=True) включает автоматический сброс оформления текста
    # от принта к принту
    tasks = get_tasks('DB.json')
    init(autoreset=True)

    menu = ''    # Переменная для работы с меню

    # Цикл для работы с меню
    while menu != '0':
        control_symbol = ['0', '1', '2', '3', '4']
        menu = ''
        while menu not in control_symbol:
            print('1 - Добавить задачу')
            print('2 - Завершить задачу')
            print('3 - Удалить задачу')
            print('4 - Текущий список задач')
            print('0 - Завершить работу с программой')
            menu = input('Введите число: ')

            if menu == '1':
                tasks = adding_tasks(tasks, 'DB.json')
            elif menu == '2':
                tasks = complete_tasks('DB.json')
            elif menu == '3':
                tasks = delete_tasks('DB.json')
            elif menu == '4':
                tasks_list('DB.json')
            elif menu != '0':
                print(Fore.RED + 'Ввод некорректен!')

# Данное условие проверяет, что приложение запущено самостоятельно,
# а не вызывается из другого файла
if __name__ == "__main__":
    main()