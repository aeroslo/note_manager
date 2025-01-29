# Функция выводит список заметок в отформатированном виде
# Для запуска используйте multiple_notes.py

import datetime
import update_status
from check_deadline import check_deadline

def display_notes(notes, show_ids = set([]), full = True):
    # функция отображения заметок,
    # первый аргумент - список со словарями заметок
    # второй - множество идентификаторов заметок для фильтрации
    # третий - визуальное отображение: полное или сокращенное

    delimiter = "\t\t" #отступ для форматирования края
    spacer = "-------------------------------------" #визуальный разделитель заметок

    print(spacer)

    if notes:

        for note in notes:

            id_number = notes.index(note) # получаем индекс заметки

            if id_number in show_ids or not show_ids:
                # проверяем что id заметки в множестве, либо аргумент множества пуст

                display_single_note(note, full, spacer, delimiter, id_number + 1)
                print(spacer)


    else:
        print("\033[31mСписок заметок пуст\033[0m")


def display_single_note(note, full, spacer, delimiter, id_number):

    print("ЗАМЕТКА №", id_number, ". ", check_deadline(note.get("Дата выполнения"))[1])
    # выводим заметку с порядковым номером и информацией о дедлайне

    print(spacer)

    for key, value in note.items():

        if key in set(["Имя", "Заголовок"]) or full is True:


            print(key + ": ")

            if isinstance(value, list):
                # если значение является списком

                for title in value:
                    print(delimiter + title)


            elif key == "Статус":
                # отдельно для подтягивания словаря статусов

                print(delimiter + update_status.status_dict.get(value))


            elif isinstance(value, datetime.date):
                # если значение дата

                print(delimiter + value.strftime('%d.%m.%Y'))


            else:
                print(delimiter + value)
