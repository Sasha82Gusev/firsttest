#Козерог: 22 декабря – 20 января
#Водолей: 21 января – 19 февраля
#Рыбы: 20 февраля – 20 марта
#Овен: 21 марта – 20 апреля
#Телец: 21 апреля – 20 мая
#Близнецы: 21 мая – 21 июня
#Рак: 22 июня – 22 июля
#Лев: 23 июля – 23 августа
#Дева: 24 августа – 23 сентября
#Весы: 24 сентября – 23 октября
#Скорпион: 24 октября – 22 ноября
#Стрелец: 23 ноября – 21 декабря
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