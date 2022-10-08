# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

print('Введите число:')
N = float(input())
N *= 10
N = int(N)
first_fractional_digit = N % 10
if first_fractional_digit == 0:
    print('-> нет')
else:
    print(first_fractional_digit)