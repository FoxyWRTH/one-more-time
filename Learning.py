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
