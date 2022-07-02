print ("Задача 1")
storona=input("Введите длинну стороны квадрата: ")
print("Площадь квадрата равна "+str(int(storona) * int(storona)))
print("Периметр квадрата равен "+str(int(storona) * 4))
print ()
a=input("Введите длинну прямоугольника: ")
b=input("Введите ширину прямоугольника: ")
print("Площадь прямоугольника равна "+(int(a) * int(b)))
print("Периметр прямоугольника равен "+str(int(a) + int(a) + int(b) + int(b)))
print ()

print ("Задача 2")
zp=int(input("Введите заработную плату в месяц: "))
ipoteka=int(input("Введите, какой процент(%) уходит на ипотеку: "))
zhiza=int(input("Введите, какой процент(%) уходит на жизнь: "))

print("На ипотеку было потрачено "+str(ipoteka * zp/100*12)+" рублей")
print("Было накоплено "+str(zp*12*(100-ipoteka-zhiza)/100)+" рублей")
print ()

print ("Задача 3")
slovo=str(input("Введите слово: "))
newslovo=slovo
newslovo=slovo[len(slovo)-1]+slovo[1:(len(slovo)-1)]+slovo[0]
print(newslovo)