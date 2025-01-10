
# Опросная форма
print("Для создания заметки аполните данные:")

field_titles=("Ваше имя", "Заголовок заметки", "Содержимое заметки", "Дата создания (ДД/ММ)", "Дата окончания (ДД/ММ)") # Кортеж с заголовками полей

note_fields = [] # обозначаем лист с данными заметки

add_title = "Y"
note_fields.insert(0,input("\t"+field_titles[0]+": ")) # принудительно назначаю индексы, чтобы не было потом путаницы
note_fields.insert(1,[]) # создаю в списке пустой список для заголовков

while add_title.lower() == "y": # добавление заголовков будет идти пока пользователь выбирает Y/y
     title=input(field_titles[1]+": ")
     note_fields[1].append(title)
     add_title=input("Добавить заголовок заметки (Y/N)?")

note_fields.insert(2, input("\t"+field_titles[2]+": "))
note_fields.insert(3,input("\t"+field_titles[3]+": "))
note_fields.insert(4,input("\t"+field_titles[4]+": "))




print("\nВы ввели следующие данные:")
print("\t"+field_titles[0]+": " + note_fields[0])
print("\t"+field_titles[1]+": "+"\n\t\t".join(note_fields[1]))
print("\t"+field_titles[2]+": " + note_fields[2])
print("\t"+field_titles[3]+": " + note_fields[3])
print("\t"+field_titles[4]+": " + note_fields[4])

print(note_fields)