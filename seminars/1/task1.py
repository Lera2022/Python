# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8, 9 -> нет

print('Введите a: ')
a = int(input())
print('Введите b: ')
b = int(input())

if a ** 2 == b or b ** 2 == a:
    print(' -> да')
else:
    print(' -> нет')