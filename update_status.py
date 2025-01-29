# Показывает текущий статус заметки.
# Предлагает изменить статус на один из предложенных.
# Обрабатывает некорректный ввод.
# Для запуска используйте multiple_notes.py


def show_status(status):
    # выводит информацию о текущем статусе заметки
    print("Текущий статус заметки: ", status_dict.get(status))

def update_status(status):
    # форма изменения статуса. Аргумент - текущий статус
    print("Введите статус заметки. Возможные варианты:")
    print("\n".join(f"{k}: {v}" for k, v in status_dict.items())) # выводим словарь статусов в читаемом виде

    while True:
        new_status = input("Для изменения статуса выберите одно из значений или оставьте поле пустым: ")
        status_value = status_dict.get(new_status)

        if new_status == status or not new_status:
          print("\033[31mСтатус не изменен. Текущий статус: " + status_dict.get(status) + "\033[0m")
          return status

        elif status_value:
            print("\033[32mУспешно. Новый статус заметки: " + status_value + "\033[0m")
            return new_status


        else:
            print("\033[31mOшибка ввода, такого варианта нет." + "\033[0m")


status_dict = {
    "1": "новая",
    "2": "в процессе",
    "3": "выполнено",
    "4": "отложено"
}


def test():
    show_status("2") #для примера вызовем функции со значением 2 (в процессе)
    update_status("2") # аргумент это значение текущего статуса (для сравнения с новым статусом)

#test() #запуск теста модулей