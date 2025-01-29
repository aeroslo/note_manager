# Удаляет заметку по имени пользователя или заголовку.
# Выводит сообщение, если заметка не найдена.
# Обновляет список заметок.
# Для запуска используйте multiple_notes.py

from display_notes_function import  display_notes

#notes = [{'Имя': 'Ivan', 'Заголовок': ['title_note 1', 'title2 note2'], 'Описание': 'description note 1', 'Статус': '1', 'Дата создания': datetime.datetime(2025, 1, 29, 7, 57, 4, 651011), 'Дата выполнения': datetime.datetime(2025, 2, 5, 7, 57, 10, 116854)}, {'Имя': 'Ivan', 'Заголовок': ['Title 1 note 2 true', 'title 2 note 2', 'title 3 note 2 '], 'Описание': 'Description 2 note', 'Статус': '2', 'Дата создания': datetime.datetime(2025, 1, 29, 7, 58, 1, 520519), 'Дата выполнения': datetime.datetime(2025, 12, 20, 0, 0)}, {'Имя': 'Maria', 'Заголовок': ['Title 1 note 3', 'title 2 note 3', 'title 3 note 3'], 'Описание': 'Description 3', 'Статус': '4', 'Дата создания': datetime.datetime(2025, 1, 29, 7, 59, 21, 299051), 'Дата выполнения': datetime.datetime(2025, 2, 5, 7, 59, 23, 970730)}]


def search_note(notes):

    search_string = input("Для удаления введите имя или название заметки: ").lower()

    match_result = set([])
    # создаем множество, куда будем помещать
    # номера заметок, подходящие под поиск

    if notes:
        for note_id in range(len(notes)):
            #перебираем индексы заметок

            name = notes[note_id].get("Имя").lower() # имя в заметке
            titles = notes[note_id].get("Заголовок") # список заголовков

            if name == search_string:
                # проверяем совпадение по имени

                match_result.add(note_id)

            for title in titles:
                # прогоняем список заголовков для проверки

                if title.lower() == search_string:
                    # проверяем заголовки на совпадение

                    match_result.add(note_id)

        return match_result


def delete_notes(notes):

    if notes:
        # если список заметок не пустой

        notes_to_delete = search_note(notes)
        # получаем множество с идентификатором заметок в поиске

        print("По запросу найдено записей:" , len(notes_to_delete))

        if notes_to_delete:
            # если найдены совпадения отображаем спиоок

            display_notes(notes, notes_to_delete, False) #запускаем вывод в сокращенном виде
            delete_now = input("Удалить найденные записи? (y / n): ").lower()

            if delete_now == "y":

                new_notes = [] # обозначаем новый пустой список

                for i in range(len(notes)):

                    if i not in notes_to_delete:
                        # если индекса нет в списке на удаление, помещаем в новый список

                        new_notes.append(notes[i])

                print("Удалено записей: ", len(notes_to_delete))
                return new_notes
    else:
        print("Cписок заметок еще пуст.")

    return notes


#delete_notes(notes)


