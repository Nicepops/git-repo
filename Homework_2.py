__author__ = 'Осипов П.Д.'

import math
import random

#easy
#1
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
for ind, elem in enumerate(fruits):
    print('{}. {}'.format(ind+1, elem))

#2
list_one = [1,2,3,4,5,11,67,4,3,8,9,6,765]
list_two = [3,11,67,9,6,4,23,6,7]

for elem in list_two:
    while elem in list_one:
        list_one.pop(list_one.index(elem))
print(list_one)

#3
original_list = [1,2,3,4,5,6,7,8,9,10,5467,2858]
end_list = []
for elem in original_list:
    if elem % 2 == 0:
        end_list.append(elem / 4)
    else:
        end_list.append(elem * 2)
print(end_list)

#normal
#1
original_list = [2, -5, 8, 9, -25, 25, 4, 121, 0]
end_list = []
for elem in original_list:
    if elem >=0 and math.sqrt(elem) % 1 == 0:
        end_list.append(int(math.sqrt(elem)))
print(end_list)

#2
days = {"01": "первое", "02": "второе", "03": "третье", "04": "четвертое", "05": "пятое", "06": "шестое",
        "07": "седьмое", "08": "восьмое", "09": "девятое", "10": "десятое", "11": "одиннадцатое",
        "12": "двенадцатое", "13": "тринадцатое", "14": "четырнадцатое", "15": "пятнадцатое", "16": "шестнадцатое",
        "17": "семнадцатое", "18": "восемнадцатое", "19": "девятнадцатое", "20": "двадцатое", "21": "двадцать первое",
        "22": "двадцать второе", "23": "двадцать третье", "24": "двадцать четвертое", "25": "двадцать пятое",
        "26": "двадцать шестое", "27": "двадцать седьмое", "28": "двадцать восьмое", "29": "двадцать девятое",
        "30": "тридцатое", "31": "тридцать первое",
}

months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
          "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря",
}
date = '02.11.2013.'
date_name = date.split('.')
print(days[date_name[0]], months[date_name[1]], date_name[2], 'года')

#3
n = int(input('Введите количество элементов списка \n'))
i = 0
list_1 = []
while i < n:
    list_1.append(random.randint(-100, 100))
    i += 1

print(list_1)

#4
#произвольное число
n = 25
i = 0
list_1 = []
list_2 = []
list_3 = []

while i < n:
    list_1.append(random.randint(-100, 100))
    i += 1
print(list_1)

for elem in list_1:
    if elem not in list_2:
        list_2.append(elem)
print(list_2)

for elem in list_1:
    if list_1.count(elem) == 1:
        list_3.append(elem)
print(list_3)

#hard
#1
equation = 'y = -12x + 11111140.2121'
x = 2.5
a = equation.split(' ')
b = str(a[2])
a[2] = b[:-1]
y = float(a[2])* x + float(a[4])
print(y)
