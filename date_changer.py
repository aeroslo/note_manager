import datetime
import re

date_str = "01-12-2025"

# Remove year from date, return user friendly date
date_list=[(date_str[0:2]),(date_str[3:5]),(date_str[6:])] # делим строку на список
date_user_friendly=date_list[0]+"/"+date_list[1] # выводим первые два значения из списка
print(date_user_friendly)


# Alternative method #1 (В этом варианте мы не привязаны к разделителям чисел на входе). Наверно очень громоздкий вариант, прошу комментов.
date = list(reversed(list(map(lambda x: int(x), (re.split(r'[-./]', date_str)))))) # регулярными делим на список, преобразуем в целочисленные, переворачиваем
date_obj = datetime.datetime(*date) #получаем объект с датой
date_user_friendly = date_obj.strftime('%d/%m') # форматируем дату как захотим
print(date_user_friendly)

# Alternative method #2
date = datetime.datetime.strptime(date_str, '%d-%m-%Y') # преобразуем строку в объект даты
date_user_friendly = date_obj.strftime('%d/%m') # форматируем дату
print(date_user_friendly)

