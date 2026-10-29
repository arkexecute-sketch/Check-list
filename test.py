# Импортируем сторонние библиотеки
import json

from edit_tasks import delete_tasks
from interface import tasks_list, get_tasks

exit_test = 1
test_tasks = get_tasks('DB_test.json')
tasks_list('DB_test.json')
while exit_test != 0:
    delete_tasks(test_tasks, 'DB_test.json')
    tasks_list('DB_test.json')
    exit_test = input('Для выхода введите "0": ')

