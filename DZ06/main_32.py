# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного 
# максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 10
arr = []

for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        arr.append(i)

print(arr)