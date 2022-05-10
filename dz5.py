documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлович"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '4': []
}

rez_shelf = None
running = True


def people(docnumber):
    for x in documents:
        # print(x['type'], '"', x['number'], '"', ' "', x['name'], '"')
        if x['number'] == docnumber:
            print(x['name'])


def list():
    for x in documents:
        print(x['type'], '"', x['number'], '"', ' "', x['name'], '"')
    print (directories)


def shelf(docnumber):
    for x in directories:
        for y in directories[x]:
            if y == docnumber:
                return (x)


def add(type, number, fio, polka):
    if polka in directories:
        documents.append({"type": type, "number": number, "name": fio})
        directories[polka].append(number)
    else:
        print('Неть такой полки, данные не добавлены')


def addshelf(ads):
    if ads in directories:
        print('Такая полка уже существует')
    else:
        #directories.update([ads]='')
        directories[ads] = []
        print('Добавили полку с номером ', ads)

def dellete(docnumber):
    not_found=True
    for x in range (len(documents)):
        # print(x['type'], '"', x['number'], '"', ' "', x['name'], '"')
        #print(documents[x])
        if documents[x]['number'] == docnumber:
            documents.pop(x)
            #del documents[x]
            not_found=False
            break

    if not_found == True:
        print('Документ  с таким номером не найден')

    for key, value in directories.items():
        if docnumber in value:
            value.remove(docnumber)

def move(docnumber,polka):
    if polka not in directories:
        print('Такая полка не существует')
    elif shelf(docnumber) == None:
        print('Докумен не найден')

    else:
        for key, value in directories.items():
            if docnumber in value:
                value.remove(docnumber)
        directories[polka].append(docnumber)



while running == True:
    command = input('Введите команду ')
    if command == 'p':
        docnumber = input('Введите номер документа ')
        people(docnumber)
    elif command == 'l':
        list()
    elif command == 's':
        docnumber = input('Введите номер документа ')

        if shelf(docnumber) == None:
            print('Докумен не найден')
        else:
            print('Полка ', shelf(docnumber))
    elif command == 'a':
        type = input('Введите тип документа ')
        number = input('Введите номер документа ')
        fio = input('Введите ФИО ')
        polka = input('На какую полку положить документ? ')
        add(type, number, fio, polka)
        list()
        if command == 'q':
        running = False
    if command == 'as':
        ads = input('Введите номер добавляемой полки ')
        addshelf(ads)
    if command == 'd':
        docnumber = input('Введите номер удаляемого документа ')
        dellete(docnumber)
    if command == 'm':
        docnumber = input('Введите номер перемещаемого документа ')
        polka = input('На какую полку переместить документ? ')
        move(docnumber,polka)
