'''
cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 1, 'measure': 'шт'},
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  'Фахитос': [
    {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'кг'},
    {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Помидор', 'quantity': 6, 'measure': 'шт'}
    ]
  }
person_count = 2

new_book={}
bludo_list=['Омлет','Фахитос']
c=1


for bl in range(int(len(bludo_list))):
    for ingr in range(int(len(cook_book[bludo_list[bl]]))):
        zz=(cook_book[bludo_list[bl]][ingr]['ingredient_name']) #Good)
        if zz in new_book.keys():
          kol=(cook_book[bludo_list[bl]][ingr]['quantity'])+(new_book[zz]['quantity']) #Good)
        else:
          kol=(cook_book[bludo_list[bl]][ingr]['quantity']) #Good)
        yy = (cook_book[bludo_list[bl]][ingr]['measure'])  # Good)
        new_book[zz]={'measure':yy,'quantity':kol}

print(new_book)

dishes = 'Омлет'

'''

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