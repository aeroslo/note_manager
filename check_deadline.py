# Запрашивает дату дедлайна и сравнивает её с текущей датой.
# Сообщает, истёк ли дедлайн или сколько дней осталось.
# Проверяет корректность формата ввода.
# Для запуска используйте multiple_notes.py


import datetime
import re


def get_now(): # возвращает объект даты
    return datetime.datetime.now()

def spell_days(days): # склоняет слово дни в зависимости от числительного
    days = abs(days)
    spell_date = [
        "дней",
        "день",
        "дня",
        "дня",
        "дня",
        "дней",
        "дней",
        "дней",
        "дней",
        "дней"
    ]

    if 10 < days < 20:
        return str(days) + " дней"
    else:
        days_index = str(days)[-1]
        spelled = spell_date[int(days_index)]
        return str(days) + " " + spelled


def check_deadline(input_date):
    # сравнивает дату аргумент с текущей датой
    # возвращает True если срок не истек и текстовый комментарий

    now = datetime.datetime.now()
    difference = now - input_date

    if difference.days == -1:
        return True, "Дедлайн завтра"
    elif difference.days == 1:
        return False, "\033[31mДедлайн прошел вчера\033[0m"
    elif input_date.date() > now.date():
        return True, "До дедлайна " + spell_days(difference.days)
    elif input_date.date() == now.date():
        return True, "Дедлайн сегодня"
    else:
        return False, "\033[31mДедлайн прошел " + spell_days(difference.days) + " назад\033[0m"


def get_date(allow_past = True):
    # запрашивает ввод даты от пользователя и проверяет на корректность
    # в качестве аргумента принимается значение allow_past, которое позволяет вводить даты ранее нынешнего момента
    while True:
        date_input = input("Введите дату дедлайна в формате ДД.ММ.ГГГГ или оставьте пустое поле,\nчтобы установить срок в 1 неделю: ")
        date_input = re.sub(r'[-./]', ".", date_input, count=0) # приводим ввод к единому формату

        if not date_input:
            auto_date = datetime.datetime.now() + datetime.timedelta(days = 7)
            return auto_date

        else:
            try:
                date_obj = datetime.datetime.strptime(str(date_input), '%d.%m.%Y')
                if date_obj < datetime.datetime.now() and not allow_past:
                    print("\033[31mДата завершения уже прошла, некорректный ввод\033[0m.")
                else:
                    return date_obj
            except:
                print("\033[31mВы ввели неверное значение даты.\033[0m")


def test():
    print("Сегодняшняя дата: ", datetime.datetime.now().strftime('%d.%m.%Y'))
    date = get_date() # запрашиваем дату
    compared_date = check_deadline(date) # сравниваем с текущей датой

    if not compared_date[0]: # Если дедлайн прошел, выдает сигнал
        print("\n\033[31mВНИМАНИЕ:\033[0m")

    print(compared_date[1]) # выводим текстовый комментарий