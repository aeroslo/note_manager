# Функция добавления единичной заметки
# Для запуска используйте multiple_notes.py

from add_titles_loop import add_names
from update_status import update_status
from check_deadline import get_now, get_date


def create_note():
    #создает новую единичную заметку

    print("\033[1mДля создания заметки заполните данные\033[0m")

    note = {
        "Имя": input("Введите ваше имя: "),
        "Заголовок": add_names([]),
        "Описание": input("Введите описание заметки: "),
        "Статус": update_status("1"), # по умолчанию заметка создается со статусом 1 - новая
        "Дата создания": get_now(),
        "Дата выполнения": get_date(False) # запрещаем вводить даты из прошлого
    }

    print("\033[1mЗаметка создана успешно!\033[0m")
    return note

