# Этот модуль отвечает за запуск приложения и работу меню

from colorama import Fore, init

# Импортируем функции из других файлов
from edit_tasks import adding_check_list, adding_tasks, complete_tasks, delete_tasks, \
    delete_check_list, adding_sub_tasks, delete_sub_tasks, complete_sub_tasks
from interface import tasks_list, get_tasks
from Class_Task import CheckList

# init(autoreset=True) включает автоматический сброс оформления текста от принта к принту
# !!!ИСПОЛЬЗУЕТСЯ СТРОГО ОДИН РАЗ ПРИ ЗАПУСКЕ ПРОГРАММЫ!!!
init(autoreset=True)

def main ():
    # Объявляем словарь с тестовыми данными
    # init (autoreset=True) включает автоматический сброс оформления текста
    # от принта к принту
    # tasks = get_tasks('DB.json')
    check_list =''
    control_symbol = []
    check_list_menu = ''
    check_lists = [CheckList('1', 'Выучить Python'),
                   CheckList('2', 'Пройти курсы')]

    # Составляем список номеров, по которым можно выбрать чек-лист
    for i in range(len(check_lists)):
        control_symbol.append(check_lists[i].serial_numb)

    # Цикл для работы программы
    while True:
        # Цикл для меню работы с чек-листами
        while check_list_menu not in control_symbol:
            # Списки символов, которые необходимо ввести
            # для добавления или удаления чек-листа
            symbol_for_add = ['д', 'Д', 'l', 'L']
            symbol_for_del = ['у', 'У', 'e', 'E']

            for i in range(len(check_lists)):
                print(f'{check_lists[i].serial_numb}. {check_lists[i].title}')

            print('Выберите чек лист по номеру')
            print('Введите "д" чтобы добавить чек лист')
            print('Введите "у" чтобы удалить чек лист')
            print('Введите 0 для выхода из программы')
            check_list_menu = input()



            if check_list_menu in control_symbol:
                check_list = check_lists[int(check_list_menu) - 1]

            elif check_list_menu in symbol_for_add:
                adding_check_list(check_lists)

            elif check_list_menu in symbol_for_del:
                check_lists = delete_check_list(check_lists)

            elif check_list_menu != '0':
                print(Fore.RED + 'Ввод некорректен!')

            if check_list_menu == '0':
                return 0

        task_menu = ''    # Переменная для работы с меню задач

        # Цикл для работы с меню задач в чек-листе
        while task_menu != '0':
            symbol_for_add = ['д', 'Д', 'l', 'L']
            symbol_for_del = ['у', 'У', 'e', 'E']
            symbol_for_complete = ['з', 'З', 'p', 'P']
            symbol_for_print = ['с', 'С', 'c', 'C']
            for i in range(len(check_list.tasks)):
                control_symbol.append(check_list.tasks[i].serial_numb)
            task_menu = ''

            while task_menu not in control_symbol and task_menu != '0':
                print('Чтобы добавить подзадачи, введите номер задачи')
                print('д - Добавить задачу')
                print('з - Завершить задачу')
                print('у - Удалить задачу')
                print('с - Текущий список задач')
                print('0 - Завершить работу с чек-листом')
                task_menu = input()

                if task_menu in symbol_for_add:
                    check_list.tasks = adding_tasks(check_list, 'DB.json')
                elif task_menu in symbol_for_complete:
                    check_list.tasks = complete_tasks(check_list)
                elif task_menu in symbol_for_del:
                    check_list.tasks = delete_tasks(check_list)
                elif task_menu in symbol_for_print:
                    tasks_list(check_list)
                    # tasks_list('DB.json')
                elif task_menu in control_symbol:
                    sub_task_menu = ''
                    while sub_task_menu != '0':
                        print('1 - Чтобы добавить подзадачу')
                        print('2 - Чтобы завершить подзадачу')
                        print('3 - Чтобы удалить подзадачу')
                        print('0 - Чтобы закончить')
                        sub_task_menu = input()

                        if sub_task_menu == '1':
                            adding_sub_tasks(check_list.tasks[int(task_menu) - 1], 'DB_test.json')
                        elif sub_task_menu == '2':
                            complete_sub_tasks(check_list.tasks[int(task_menu) - 1])
                        elif sub_task_menu == '3':
                            delete_sub_tasks(check_list.tasks[int(task_menu) - 1])
                        elif sub_task_menu == '0':
                            task_menu = ''

                elif task_menu == '0':
                    check_list_menu = ''
                elif task_menu != '0':
                    print(Fore.RED + 'Ввод некорректен!')

# Данное условие проверяет, что приложение запущено самостоятельно,
# а не вызывается из другого файла
if __name__ == "__main__":
    main()