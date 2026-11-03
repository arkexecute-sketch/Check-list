def delete_check_list(check_lists):
    check_list_id = -1

    # Цикл, который требует от пользователя ввести номер задачи для удаления
    while 0 >= check_list_id or check_list_id > len(check_lists):
        try:
            check_list_id = int(
                input('Введите номер задачи,'
                      ' которую хотите удалить (0 - для отмены): '))

            if check_list_id > len(check_lists):
                print('Задачи с таким номером не существует!')
            elif check_list_id == 0:
                return check_lists

        except ValueError:
            check_list_id = -1
            print('Нужно ввести целое число!')

    # Если задача, введенная пользователем последняя в списке,
    # то мы просто удаляем ее, не заходя в цикл перезаписи.
    # Иначе:
    # Проходимся по всем задачам после той, которую нужно удалить.
    # Перезаписываем все задачи после удаленной, чтобы они поднялись по порядковому номеру
    if check_list_id == len(check_lists):
        del (check_lists[check_list_id - 1])
        print(f'Задача №{check_list_id} успешно удалена')
    else:

        for k in range(check_list_id - 1,
                       len(check_lists) - 1):
            check_lists[k] = check_lists[k + 1]
            check_lists[k].serial_numb -= 1
        check_lists.pop()
        print(f'Задача №{check_list_id} успешно удалена')

    # save_in_json(tasks, db_file)
    return check_lists

