# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

print('Введите число 1:')
max = int(input())

for i in range(2, 6):
    print('Введите число', i, ' :')
    a = int(input())
    if a > max:
        max = a
print('max = ', max)