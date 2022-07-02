print('Задание 1')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
for count_ in range(len(geo_logs)):
    # a='visit'+str(count_+1)
    if (geo_logs[count_]['visit' + str(count_ + 1)][1]) == 'Россия':
        print(geo_logs[count_])

print('')
print('Задание 2')
newlist = []
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
for count1 in range(len(ids)):
    # print(ids['user'+str(count+1)])
    for count2 in range(len(ids['user' + str(count1 + 1)])):
        id_ = (ids['user' + str(count1 + 1)][count2])
        if id_ not in newlist:
            newlist.append(id_)
print(newlist)

print('')
print('Задание 3')
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'новые рецепты пасхальных куличей',
    'куда поехать отдыхать этим летом',
    'погода',
    'очень длинный запрос из много много много слов',
    'тра тат та'
]
dict_zapr = {}
x = 1
temp_ = 0
for z in range(len(queries)):
    zapros = queries[z]

    for y in range(len(zapros)):
        if zapros[y] == ' ':
            x = x + 1  # колличество слов
    #print('Запрос ', z + 1, '-->', x, ' слова')
    if x in dict_zapr.keys():
        dict_zapr[x] += 1
    else:
        dict_zapr[x] = 1

    x = 1

for pers, zapr in dict_zapr.items():
    print('Запросов из ', pers, ' слов', round(((zapr * 100) / (len(queries))), 2), '%')

print('')
print('Задание 4 ')
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max=0
for key,value in stats.items():
    if value > max:
        maxss=key
        max=value
print (maxss)

print('')
print('Задание 5, решение найденное в интернете и не до конца понятое ')

list=['2018-01-01', 'yandex', 'cpc', 100]
dic={}
dic={list[-2]:list[-1]}
for h in list[:-2][::-1]:
    dic={h:dic}

print(list)
print(dic)