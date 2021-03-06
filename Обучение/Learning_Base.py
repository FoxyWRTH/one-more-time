from colorama import init, Fore, Style

init()

# Задача 2.1
# Сохраните текстовое сообщение в переменной и выведите его на экран.
print(Fore.GREEN + "Задача 2.1" + Style.RESET_ALL)
doll = "Координаты получены, ожидаем команды."
print(doll)
# Это проще простого, в этой задаче даже комментировать нечего.

# Задача 2.2
# Сохраните сообщение в переменной и выведите это сообщение. Затем замените значение переменной другим
# сообщением и выведите новое сообщение.
print(Fore.GREEN + "Задача 2.2" + Style.RESET_ALL)
doll_2 = "Бессмысленная рутина - разрушает разум."
print(doll_2)
doll_2 = "Осмысленная рутина - тренирует его."
print(doll_2)
# Это проще простого, в этой задаче даже комментировать нечего.

# Задача 2.3
# Сохраните имя пользователя в переменной и выведите сообщение, предназначенное для конкретного человека.
# Сообщение должно быть простым — например, "Hello Eric, would you like to learn some Python today?”.
print(Fore.GREEN + "Задача 2.3" + Style.RESET_ALL)
name_person = "Лис"
print(f"Привет {name_person}, как проходит твоё обучение?")
# Используя приём форматирования "f" это не составило труда.

# Задача 2.4
# Сохраните имя пользователя в переменной и выведите его в нижнем регистре, в верхнем регистре и с
# капитализацией начальных букв каждого слова.
print(Fore.GREEN + "Задача 2.4" + Style.RESET_ALL)
name_person = "Лис"
print(name_person.lower())
print(name_person.upper())
print(name_person.title())
# Используя "lower" "upper" "title" - не составляет труда.

# Задача 2.5
# Найдите известное высказывание, которое вам понравилось. Выведите текст цитаты с именем автора.
# Результат должен выглядеть примерно так (включая кавычки): Albert Einstein once said, "A person who never made a
# mistake never tried anything new."
print(Fore.GREEN + "Задача 2.5" + Style.RESET_ALL)
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
# Проще простого, используя одинарные кавычки, можно вносить двойные и наоборот.

# Задача 2.6
# Повторите упражнение 2.5, но на этот раз сохраните имя автора цитаты в переменной famous_person. Затем
# составьте сообщение и сохраните его в новой переменной с именем message. Выведите своё сообщение.
print(Fore.GREEN + "Задача 2.6" + Style.RESET_ALL)
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(f"{famous_person} once said, {message}")
# Используя знания о форматировании "f" и одинарных и двойных кавычках, с заданием легко справиться.

# Задача 2.7
# Сохраните имя пользователя в переменной. Добавьте в начале и в конце имени несколько пропусков.
# Проследите за тем, чтобы каждая служебная последовательность , "\t" и "\n", встречалась по крайней мере один раз.
# Выведите имя, чтобы были видны пропуски в начале и конце строки. Затем выведите его снова с использованием каждой
# из функций удаления пропусков: lstrip(), rstrip() и strip().
print(Fore.GREEN + "Задача 2.7" + Style.RESET_ALL)
name_person_1 = "   Лис"
name_person_2 = "Лис   "
name_person_3 = "    Лис  "
print(name_person_1, "\t", name_person_2, "\n", name_person_3)
print(f"{name_person_1.lstrip()} {name_person_2.rstrip()} {name_person_3.strip()}")
# Странное задание, но суть я понял, работа "Стрипов" усвоена.

# Задача 2.8
# Напишите операции сложения, вычитания, умножения и деления, результатом которых является число 8. Не
# забудьте заключить операции в команды print(), чтобы проверить результат. Вы должны написать четыре строки кода,
# которые выглядят примерно так: print(5 + 3) Результатом должны быть четыре строки, в каждой из которых выводится
# число 8.
print(Fore.GREEN + "Задача 2.8" + Style.RESET_ALL)
print(5 + 3)  # Сложение.
print(10 - 2)  # Вычитание.
print(16 / 2)  # Деление.
print(4 * 2)  # Умножение.
# Несложно.

# Задача 3.2
# Выберите свой любимый вид транспорта (например, мотоциклы или машины) и создайте список с примерами.
# Используйте свой список для вывода утверждений об элементах типа: «Я хотел бы купить мотоцикл Honda».
print(Fore.GREEN + "Задача 3.2" + Style.RESET_ALL)
names_weapon = ['PP-19', 'AK-74', 'AEK-971']
print(f"Лучшее оружие для стрельбы по гражданским в замкнутых пространствах: {names_weapon[0]}")
print(f"Лучшее оружие в соотношении цена - качество: {names_weapon[1]}")
print(f"Просто хороший автомат: {names_weapon[2]}")

weapons_list = []  # Создание пустого списка.

weapons_list.insert(0, "M4")  # "insert" добавляет в список элемент с указанием в какую позицию, остальные смещаются.
weapons_list.insert(1, "HK416")
weapons_list.append("AK47")  # "append" добавляет в список элемент всегда в конец списка, остальные неподвижны.
weapons_list.append("RPK74")
# del weapons_list[0]  # "del" Удаляет элемент из списка, обязательное условие: нужен индекс, остальные смещаются.
# weapons_list.pop()  # "pop" Вынимает последний элемент из списка, позволяя обращаться к нему позже. Если задать
# индекс, вынет определённый элемент.
# weapons_list.remove()  # "remove" Убирает элемент указанный в скобках,
# поиск производится не по индексу, а содержанию. Может передавать его в переменную для дальнейшего использования.
print(weapons_list)

# Задача 3.4
# Если бы вы могли пригласить кого угодно (из живых или умерших) на обед, то кого бы вы пригласили? Создайте список,
# включающий минимум трёх людей, которых вам хотелось бы пригласить на обед. Затем используйте этот список для вывода
# пригласительного сообщения каждому участнику.
print(Fore.GREEN + "Задача 3.4" + Style.RESET_ALL)
names_of_guests = ["Peter", "Marlow", "Luter", "Alice", "Mia"]
print(f"Dear {names_of_guests[0]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[1]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[2]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[3]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[4]} come to me house and drink with me vodka!")
# Списки, индексы, усвоил.

# Задача 3.5
# Вы только что узнали, что один из гостей прийти не сможет, поэтому вам придётся разослать новые приглашения.
# Отсутствующего гостя нужно заменить кем-то другим.
# • Добавьте в конец программы команду print для вывода имени гостя, который прийти не сможет.
# • Измените список и замените имя гостя, который прийти не сможет, именем нового приглашенного.
# • Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.
print(Fore.GREEN + "Задача 3.5" + Style.RESET_ALL)
not_came = names_of_guests.pop(2)
print(f"{not_came} don't drink vodka...")
names_of_guests.insert(2, "Elena")
print(f"Dear {names_of_guests[0]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[1]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[2]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[3]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[4]} come to me house and drink with me vodka!")
# Списки, замены, вроде усвоил, надо будет подглядывать пока не запомню.

# Задача 3.6
# Вы решили купить обеденный стол большего размера. Дополнительные места позволяют пригласить на обед еще трех гостей.
print(Fore.GREEN + "Задача 3.6" + Style.RESET_ALL)
print(Fore.YELLOW + f"We need more guys and girls, and we need more booze." + Style.RESET_ALL)
names_of_guests.insert(0, "Alex")
names_of_guests.insert(3, "Julie")
names_of_guests.append("Toni")
names_of_guests.append("Luter")
print(f"Dear {names_of_guests[0]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[1]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[2]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[3]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[4]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[5]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[6]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[7]} come to me house and drink with me vodka!")
print(f"Dear {names_of_guests[8]} come to me house and drink with me all what you want!")

# Задача 3.7
# Все приглашённые гости, летели к вам на вечеринку в одном самолёте, который потерпел крушение где-то посреди
# атлантического океана. Мир праху их.
print(Fore.GREEN + "Задача 3.6" + Style.RESET_ALL)
names_of_dead = names_of_guests.pop()
print(Fore.RED + f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}")
names_of_dead = names_of_guests.pop()
print(f"R.I.P {names_of_dead}" + Style.RESET_ALL)
print(Fore.YELLOW + f"Well, {names_of_guests[0]} and {names_of_guests[1]}, let's drink for dead!" + Style.RESET_ALL)
del names_of_guests[0]
del names_of_guests[0]
print(f"When they got drunk, they didn't share a bottle and killed each other, leaving alive...", len(names_of_guests))
print(Fore.RED + f"Conclusion, alcohol is evil." + Style.RESET_ALL)

# Сортировка.
print(Fore.GREEN + "Сортировка" + Style.RESET_ALL)

weapons_list = ["M4", "RPK74", "HK416", "AK47", "PP19", "M16", "SVD"]
print(weapons_list)
print(sorted(weapons_list), "Временная сортировка")  # Временная сортировка.
print(sorted(weapons_list, reverse=True), "Временная Обратная сортировка")
weapons_list.sort()  # Постоянная сортировка списка.
print(weapons_list, "Постоянная сортировка")
weapons_list.sort(reverse=True)  # Постоянная обратная сортировка списка.
print(weapons_list, "Постоянная обратная сортировка")

weapons_list = ["M4", "RPK74", "HK416", "AK47", "PP19", "M16", "SVD"]
weapons_list.reverse()  # Не сортирует, а просто разворачивает список задом наперёд.

# Циклы.
print(Fore.GREEN + "Циклы" + Style.RESET_ALL)
for weapon in weapons_list:
    print(Fore.YELLOW + weapon + Style.RESET_ALL, f"this weapon can kill people!")
    print(Fore.RED + "KILL THEM ALL!!!" + Style.RESET_ALL)
print(f"Just use this weapon to kill people, all people.")

print(Fore.GREEN + "Задача 4.1" + Style.RESET_ALL)
names_of_gods = ["Tzeentch", "Nurgle", "Khorne", "Slaanesh"]
for chaos_god in names_of_gods:
    print(Fore.LIGHTBLUE_EX + f"{chaos_god}" + Style.RESET_ALL + " is God of chaos.")
print(Fore.RED + f"And let the galaxy, burn." + Style.RESET_ALL)

print(Fore.GREEN + "Диапазон" + Style.RESET_ALL)
wtf_num = list(range(2, 12, 3))  # Диапазон, аргументы (2 - от чего начинать, 12 конечная точка, 3 сколько добавить)
print(wtf_num)

print(Fore.GREEN + "Цикл (Возведение во 2ю степень)" + Style.RESET_ALL)
step_2 = []
for i in range(1, 11):
    step_2.append(i ** 2)
print(step_2)

print(Fore.GREEN + "Цикл (Возведение во 2ю степень, однострочное)" + Style.RESET_ALL)
step_2_v_2 = [numba ** 2 for numba in range(1, 11)]
print(step_2_v_2)

print(Fore.YELLOW + "Задачи на циклы" + Style.RESET_ALL)
print(Fore.GREEN + "Задача 4.3 Используйте цикл for для вывода чисел от 1 до 20 включительно." + Style.RESET_ALL)

numba_list = []
for i in range(1, 21):
    numba_list.append(i)
print(numba_list, "Блок")

numba_list = [i for i in range(1, 21)]
print(numba_list, "Однострочный")

print(Fore.YELLOW + "Работа с частями списка" + Style.RESET_ALL)
print(Fore.GREEN + "Задача 4.10 Первые три сегмента списка." + Style.RESET_ALL)
numba_list = [i for i in range(1, 11)]
print("Сам список:", numba_list)
print('Первые 3 сегмента:', numba_list[0:3])
print('Средние 3 сегмента:', numba_list[3:7])
print('Последние 3 сегмента:', numba_list[-3:])

print(Fore.GREEN + "Задача 4.11 Копирование списков" + Style.RESET_ALL)

numba_list_1 = [i for i in range(1, 11)]
numba_list_2 = [i for i in range(11, 21)]
print(f"Первый список", numba_list_1)
print(f"Второй список", numba_list_2)

print(Fore.GREEN + f"В список 1, скопирован список 2" + Style.RESET_ALL)
numba_list_1 = numba_list_2[:]
print(numba_list_1)
print(numba_list_2)

numba_list_1.append(774)
numba_list_2.append(992)
print(Fore.GREEN + f"В списки добавлены разные значения, они различны" + Style.RESET_ALL)
print(numba_list_1)
print(numba_list_2)
print(Fore.GREEN + f"Это доказывает что произведено именно копирование а не слияние." + Style.RESET_ALL)
print(Fore.GREEN + f"Печать списка 1 с помощью цикла" + Fore.YELLOW + " 'for'" + Style.RESET_ALL)
for i in numba_list_2:
    print(i)
print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.YELLOW + f"Команды 'IF' Это уже гораздо интереснее." + Style.RESET_ALL)

print(Fore.GREEN + f"Задача вывести список машин, "
                   f"Названия должны быть с большой буквы, марка BMW только большими." + Style.RESET_ALL)

cars = ["audi", "reno", "Bmw", 'lada']
for i in cars:
    if i.lower() == "bmw":  # Что бы не зависеть от регистра, там где он не важен, заранее занижаем его.
        print(i.upper())
    else:
        print(i.title())

print(Fore.YELLOW + f"Проверка на возраст" + Style.RESET_ALL)

# age = input("Введи свой возраст: \n")
#
# if not age.isdigit():  # Используется проверка, вводится ли число или строка.
#     print('Вы ввели не корректные данные')
# elif int(age) <= 17:
#     print("Ты слишком мал, приходи позже.")
# elif 18 >= int(age) <= 59:
#     print('Всё отлично, заходи.')
# elif int(age) >= 60:
#     print('Дедуль, а ты потянешь?')

age = 32
if age <= 17:
    print('To young...')
elif age >= 17:
    print('All is good.')
elif age >= 65:
    print('To old...')
else:
    print('WTF?')

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.YELLOW + f"Наполнение списка" + Style.RESET_ALL)

# Вот таким образом можно наполнить список, не вводя кавычки и прочие разделители.

# some_list = []
#
# for x in range(5):
#     i = input('Вводи наполнение списка.\n')
#     some_list.append(i)
#
# print(some_list, type(some_list))

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.GREEN + f"Внесение компонентов в список, последующий перебор для сравнения, "
                   f"возврат значений." + Style.RESET_ALL)
#
#
# topi_avail = []
# topi_request = []
#
# avail = 1
# request = 1
#
# while avail <= 3:
#     avail = avail+1
#     topi_avail.append(input('What we have? \n').lower())
#
# while request <= 3:
#     request = request+1
#     topi_request.append(input('What you want? \n').lower())
#
# for topi_request in topi_request:
#     if topi_request in topi_avail:
#         print(f'Ok, added {topi_request}')
#     else:
#         print(f'We not have {topi_request}')
#
print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.GREEN + f"Перебор значений в списке, отдельная реакция на определённое значение." + Style.RESET_ALL)

some_tags = ['WE', 'DS', 'SS', 'AA', 'ADM', 'WDD']

for i in some_tags:
    if i != 'ADM':
        print(f'hello {i}, go kill yourself!')
    else:
        print('Hello Foxy! Nice to see you!')

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.GREEN + f"Проверка на успешное опустошение списка и вывод подтверждения." + Style.RESET_ALL)

some_tags = ['WE', 'DS', 'SS', 'AA', 'ADM', 'WDD']

some_tags.clear()

if len(some_tags) == 0:
    print(f"it's empty!")
else:
    print(f"Something here!")

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.GREEN + f"Сравнение двух списков, добавление отсутствующих. Сортировка." + Style.RESET_ALL)

some_tags = ['we', 'ds', 'ss', 'aa', 'adm', 'wdd']
some_tags_2 = ['WE', 'ADS', 'SSS', 'ADA', 'ADM', 'ADD']

for some_tags_2 in some_tags_2:
    if some_tags_2.lower() in some_tags:
        print(f'{some_tags_2}, have here!')
    else:
        some_tags.append(some_tags_2.lower())
        print(f'{some_tags_2}, added!')

some_tags.sort()

print(some_tags)

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

print(Fore.GREEN + f"Пронумеровать окончания лет. Сделал 2 решения, думаю можно ещё короче." + Style.RESET_ALL)

numba = [i for i in range(1, 36)]

for i in numba:
    if i % 10 == 1 and i != 11:
        print(i, 'год')
    elif 2 <= i % 10 <= 4 and i != 12 and i != 13 and i != 14:
        print(i, 'года')
    elif 5 <= i % 10 <= 9 or i % 10 == 0 or 11 <= i <= 14:
        print(i, 'лет')
    else:
        print(i, 'WTF???')

for i in numba:
    if i % 10 == 1 and i != 11:
        print(i, 'год')
    elif 2 <= i % 10 <= 4 and not (12 <= i <= 14):
        print(i, 'года')
    elif 5 <= i % 10 <= 9 or i % 10 == 0 or 11 <= i <= 14:
        print(i, 'лет')
    else:
        print(i, 'WTF???')

print(Fore.GREEN + f"Задача выполнена." + Style.RESET_ALL)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow', 'points': 5}
print(f'Start position of alien: X - {alien_0["x_position"]}, Y - {alien_0["y_position"]}')

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'normal':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'New Alien position: {alien_0["x_position"]}')

alien_0['speed'] = 'fast'

print(alien_0)

del alien_0['points']  # При удалении ключа — удаляется и значение. Эффект не обратим.

print(alien_0)

key_station = {'color_1': 'green', 'color_2': 'red',
               'color_3': 'yellow', 'color_4': 'black',
               'color_5': 'pink', 'color_6': 'violet',
               'color_7': 'white', 'color_8': 'indigo'}

print(key_station)

key_station['color_5'] = 'blue'  # Добавление ключ — значение в словарь.

print(Fore.GREEN + f'My favorite color is: {Fore.RED + key_station["color_2"] + Style.RESET_ALL}' + Style.RESET_ALL)

# С помощью функции "get" можно проверять есть ли ключ в словаре.
print(key_station.get('color_9', Fore.LIGHTMAGENTA_EX + 'Nothing here!' + Style.RESET_ALL))
# В первом аргументе сообщается ключ, во втором, что вывести если отсутствует.

# Множественное присваивание! О_о
# name, age, region = input('Имя?'), input('Возраст?'), input('Регион?')
#
# print(f'Твоё имя: {name} Твой возраст: {age} Твой регион: {region}')

user_name = {'Login': 'FXR',
             'Firs_Name': 'Foxy',
             'Last_name': 'WRTH'}

favorite_language = {'Foxy': 'Python',
                     'Alice': 'Ruby',
                     'Dani': 'Java',
                     'Lisa': '1C',
                     'Mark': 'Python',
                     'Julia': 'C++',
                     'Jan': 'C++'}

for key, value in favorite_language.items():  # Перебор ключей и значений.
    print(f'Name: {key} | Language: {value}')

friends_name = ['Foxy', 'Alice']

for name in favorite_language.keys():  # Проверка наличия ключей friends_name в словаре и вывод значений.
    print(name.title())
    if name in friends_name:
        language = favorite_language[name.title()]
        print(f'Hi! {name}, I see your language: {language}')

people_name = ['Foxy', 'Alice', 'Dani', 'Lisa', 'Mark', 'Julia', 'Jan', 'Alex', 'Toni']

for name in people_name:  # Проверка наличия ключей friends_name в словаре и вывод значений.
    if name in favorite_language.keys():
        print(f'Hi {name}, thank you for join us!')
    elif name not in favorite_language.keys():
        print(f'Dear {name}! Join us!')

if 'Erl' not in favorite_language.keys():  # Проверка на отсутствие по ключу.
    print(f'WTF "Erl"? Go fuck yourself!')

for value in set(favorite_language.values()):  # Set - Устраняет повторения.
    print(f'Language is {value}')

# 6.3
# Глоссарий: словари Python могут использоваться для моделирования «настоящего» словаря (чтобы не создавать
# путаницу, назовём его глоссарием):
# Вспомните пять терминов из области программирования, которые вы узнали в
# предыдущих главах. Используйте эти слова как ключи глоссария, а их определения — как значения.
# Выведите каждое слово и его определение в аккуратно отформатированном виде.
# Например, вы можете вывести слово, затем двоеточие и определение или же слово в одной строке,
# а его определение — с отступом в следующей строке. Используйте символ
# новой строки (\n) для вставки пустых строк между парами «слово — определение» в выходных данных.

some_data = {"1st": "Do what you can.",
             "2nd": "Don't be a lazy fox!",
             "3rd": "Don't give up.",
             "4th": "Just do it.",
             "5th": "Yes you can!",
             "6th": "Make your dreams come true!",
             "7th": "Nothing is impossible!"}

for key, value in some_data.items():
    print(f"Rule {key}: {value}")
