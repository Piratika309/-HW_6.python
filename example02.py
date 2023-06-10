# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)

import random
list = []
for i in range(10):
    list.append(random.randint(1, 100))
print(list)

min_number = int(input('Введите минимальное значение: '))
max_number = int(input('Введите максимальное значение: '))

for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)