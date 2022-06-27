from colorama import init, Fore, Style

init()

print(Fore.YELLOW + 'Это место, в котором проводятся небольшие исследования/уточнения.' + Style.RESET_ALL)

# key_station['color_5'] = 'blue'  # Добавление ключ — значение в словарь.

favorite_language = {'Foxy': 'Python',
                     'Alice': 'Ruby',
                     'Dani': 'Java',
                     'Lisa': '1C',
                     'Mark': 'Python',
                     'Julia': 'C++',
                     'Jan': 'C++'}

aliens = []

for i in range(30):
    new_alien = {'Color': 'Green', 'Speed': 'Normal', 'Damage': 5}
    aliens.append(new_alien)

for i in aliens[:5]:
    print(i)
print('...')
print(f'Total aliens {len(aliens)}')

for i in aliens[:3]:
    if i['Color'] == 'Green':
        i['Color'] = 'Red'
        i['Speed'] = 'Fast'

for i in aliens[:5]:
    print(i)
print('...')
