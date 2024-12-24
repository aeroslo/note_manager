import datetime

# Опросная форма
print(f"Заполните данные:")


# Вариант 1
username = input("\tВаше имя: ")
title = input("\tНазвание заметки: ")
content = input("\tСодержимое заметки: ")
created_date = datetime.datetime.now().strftime('%d/%m')
issue_date = input("\tДата окончания в формате ДД/ММ: ")

print("\nВы ввели следующие данные:")
print("\tВаше имя: " + username)
print("\tНазвание заметки: " + title)
print("\tСодержимое заметки: " + content)
print("\tДата создания (присвоено автоматически): " + created_date)
print("\tДата окончания: " + issue_date)


# Вариант 2
data=["Ваше имя","Название заметки","Содержимое заметки","Дата окончания в формате ДД/ММ"]
data_dict = {}
created_date = datetime.datetime.now().strftime('%d/%m')

for message in data:
    data_dict[message]=input("\t" + message + ": ")

print("\nВы ввели следующие данные в заметке от "+created_date+":")
for message in data:
        print("\t" + message + ": "+data_dict[message])

