#   Создаёт несколько заметок через ввод данных
#   (имя, заголовок, описание, статус, дату создания, дедлайн).
#   Хранит заметки в списке словарей.



from create_note_function import create_note
from display_notes_function import display_notes
from delete_note import delete_notes

print("\033[1mДобро пожаловать в менеджер заметок.\033[0m")

notes = []

while True:

    answer = input("\033[34m\nВозможные действия:\n"
                   "1. Добавить заметку\n"
                   "2. Отобразить существующие заметки\n"
                   "3. Удалить заметку\n"
                   "4. Завершить работу и выйти\n\033[0m")

    if answer == "1":

        notes.append(create_note())  # добавляем в список новую заметку

    elif answer == "2":

        display_notes(notes)

    elif answer == "3":

        notes = delete_notes(notes)

    elif answer == "4":

        break


#print(notes)

