print("Задание 1")
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard','Dima']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha','Zina']

if (len(boys)==len(girls)):

    boys.sort()
    girls.sort()
    res = zip(boys,girls)
    print("Идеальные пары:")
    for zboys, zgirls in zip(boys, girls):
        print(zboys," и ", zgirls)

else:
    print("Кто-то может остаться без пары!")

print("")
print("Задание 2")
pers=5
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]

  ],
    ['Блины',
     [
         ['мука', 200, 'гр.'],
         ['яйца', 4, 'шт.'],
         ['соль', 6, 'гр.'],
         ['сахар', 40, 'гр.'],
         ['молоко', 400, 'мл.'],
     ]

     ]

]
#print(len(cook_book))
for meal, ingredients in cook_book:
    print('')
    print (meal)
    for ingredient, weight, gr in ingredients:
        print(ingredient,',',weight*pers, gr)