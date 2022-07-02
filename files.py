
# Задание 1
with open('recipes.txt') as f:
    eof = False #конец файла
    cook_book = {}
    sostav = []
    while eof == False:
        bludo = f.readline().strip()
        count = f.readline().strip()
        for i in range(int(count)):
            stroka=f.readline().strip()
            razb = stroka.split(' | ')
            ingredient = razb[0]
            x = int(razb[1])
            unit = razb[2]
            sostav.append({'ingredient_name': ingredient, 'quantity': x, 'measure': unit})
        cook_book[bludo] = sostav
        sostav=[]
        eob = f.readline()
        if eob == '':
            eof = True



#print(cook_book) Выводим результат задания 1


# Задание 2

def get_shop_list_by_dishes(bludo_list, person_count):
    new_book = {}
    for bl in range(int(len(bludo_list))):
        for ingr in range(int(len(cook_book[bludo_list[bl]]))):
            zz = (cook_book[bludo_list[bl]][ingr]['ingredient_name'])
            if zz in new_book.keys():
                kol = (cook_book[bludo_list[bl]][ingr]['quantity'])*person_count + (new_book[zz]['quantity'])
            else:
                kol = (cook_book[bludo_list[bl]][ingr]['quantity'])*person_count
            yy = (cook_book[bludo_list[bl]][ingr]['measure'])
            new_book[zz] = {'measure': yy, 'quantity': kol}
    return new_book



person_count = int(input('Введите количество человек: '))
bludo_list = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')

get_shop_list_by_dishes(bludo_list, person_count)


# Задание №3

source_files=['11.txt','22.txt','33.txt','44.txt'] # список исходных файлов
newfile = open('itog.txt','w') #итоговый файл

spisfiles={} #Создаем словарь со списком файлов и количеством строк в них
for file in source_files:
    lines = 0
    opened_file = open(file)
    for line in opened_file:
        lines += 1
    spisfiles[file]=lines
    opened_file.close()
#print(spisfiles)

sorted_tuple = sorted(spisfiles.items(), key=lambda x: x[1]) #сортируем словарь по количеству строк в файлах
sorteddict=dict(sorted_tuple)
#print(sorteddict)

#пишем новый файл
for i in sorteddict:
    newfile.write(i + '\n')
    newfile.write(str(sorteddict[i])+'\n')
    newfilestr=open(i)
    for gg in range (int((sorteddict[i]))):
        wrstr=(newfilestr.readline().strip())
        newfile.write(wrstr+'\n')
    newfilestr.close()
newfile.close()
