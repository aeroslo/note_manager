import datetime

# Опросная форма
print(f"Заполните данные:")


titles = [] # обозначаем лист с будущими заголовками

username = input("\tВаше имя: ")
add_title = "Y"

while add_title.lower() == "y":
    title = input("\tЗаголовок заметки: ")
    titles.append(title)
    add_title=input("Добавить заголовок заметки (Y/N)?")

content = input("\tСодержимое заметки: ")
created_date = datetime.datetime.now().strftime('%d/%m')
issue_date = input("\tДата окончания в формате ДД/ММ: ")

print("\nВы ввели следующие данные:")
print("\tВаше имя: " + username)
print("\tЗаголовок заметки: "+"\n\t\t".join(titles))
print("\tСодержимое заметки: " + content)
print("\tДата создания (присвоено автоматически): " + created_date)
print("\tДата окончания: " + issue_date)