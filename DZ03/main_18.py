# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5


n = int(input("Введите длинну массива = "))
arr = list(map(int, input("Введите массив черезз пробел = ").split()))
x = int(input("Ищём ближайшее число для = "))

print(arr)

f = arr[0]
for i in range(1, n):
    if abs(arr[i] - x) < abs(f - x):
        f = arr[i]

print("Ближайшее число к ",x," =",f)