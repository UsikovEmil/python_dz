# Задача 28: Напишите рекурсивную функцию sum(A, B), 
# возвращающую сумму двух целых неотрицательных чисел. Из 
# всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# 2 2
# 4

def sum(A, B):
    if B == 0:
        return A
    else:
        return sum(A ^ B, (A & B) << 1)
    
a = int(input("Введите число A = "))
b = int(input("Введите число B = "))    
print("Сумма чисел =",sum(a,b))