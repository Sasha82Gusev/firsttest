print ("Задание 1")
print ("63-Самарская область")
print ("02-Республика Башкортостан")
print ("89-Ямало-Ненецкий автономный округ")
print ("82-Республика Крым")
print ("65-Сахалинская область")
print ("03-Республика Бурятия")
print ("87-Чукотский автономный округ")
print ("16-Республика Татарстан")
bs = float(7);
region=(input("Введите код региона: "))
dvregions = {'65':'Сахалинская область','03':'Республика Бурятия','87':'Чукотский автономный округ'}
otherregions = {'63': 'Самарская область', '02': 'Республика Башкортостан','89': 'Ямало-Ненецкий автономный округ','82':'Республика Крым','16':'Республика Татарстан'}
if region in dvregions:
    bs=float(2);
    print("Ставка для вас ", bs, '%')
elif region in otherregions:
    children=int((input("Сколько у вас детей? ")))
    if children > 3:
        bs=bs-1
    zp = str((input("У вас есть зарплатный проект в нашем банке? (да/нет)")))
    if zp=="да":
        bs = bs - 0.5
    strah = str((input("Будете оформлять страховку? (да/нет)")))
    if strah=="да":
        bs = bs - 1.5
    print("Ставка для вас ", bs, '%')
else:
    print ("Нет такого региона")

print ("Задание 2")
dat=int((input("Введите число: ")))
month=str((input("Введите месяц: ")))
if (month == "декабрь" and dat > 21) or (month == "январь" and dat < 21):
    print("Козерог")
if (month == "январь" and dat > 20) or (month == "февраль" and dat < 20):
    print("Водолей")
if (month == "февраль" and dat > 19) or (month == "март" and dat < 21):
    print("Рыбы")
if (month == "март" and dat > 20) or (month == "апрель" and dat < 21):
    print("Овен")
if (month == "апрель" and dat > 20) or (month == "май" and dat < 21):
    print("Телец")
if (month == "май" and dat > 20) or (month == "июнь" and dat < 22):
    print("Близнецы")
if (month == "июнь" and dat > 21) or (month == "июль" and dat < 23):
    print("Рак")
if (month == "июль" and dat > 22) or (month == "август" and dat < 24):
    print("Лев")
if (month == "август" and dat > 23) or (month == "сентябрь" and dat < 24):
    print("Дева")
if (month == "сентябрь" and dat > 23) or (month == "октябрь" and dat < 24):
    print("Весы")
if (month == "октябрь" and dat > 23) or (month == "ноябрь" and dat < 23):
    print("Скорпион")
if (month == "ноябрь" and dat > 22) or (month == "декабрь" and dat < 22):
    print("Стрелец")

print("")
print("Задание 3")
print("К следующей лекции прочитал про циклы for и while")
