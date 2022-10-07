# # print('hello world')


# # типы данных и переменная
# # int, float, boolean, str, list, None
# value = None
# # print(type(value))

# # print(type(a))
# # print(type(b))
# value = 12334
# # print(type(value))
# a = 123
# b = 1.23
# s = 'hello world'

# print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)
# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **, ⊕, ⊖, *, /, //, %, +, -
# (), Сокращённые операции

# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a *= 5

# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ̂
# is, is not, in, not in
# gen

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = [1, 2, 3, 4]
# print (f)
# print (not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input ('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Управляющие конструкции
# while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции
# for

# r = range(1, 5, 2)# [1, 2, 3, 4, 10, 5]
# for i in 'qwe - rty':
#     print(i)

from http.client import FORBIDDEN
import numbers


# print(len(text))                    # 39
# print('ещё' in text)                # true
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('ещё', 'ЕЩЁ'))

# for c in text:
#     print(c)
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])              # с
# print(text[1])              # ъ
# # print(text[len(text)])      # IndexError
# print(text[len(text)-1])    # к
# print(text[-5])             # б
# print(text[:])              # съешь ещё этих мягких французских булок
# print(text[:2])              # съ
# print(text[len(text)-2:])   # ок
# print(text[2:9])            # ешь ещё
# print(text[6:-18])          # ещё этих мягких
# print(text[0:len(text):6])  # сеикал
# print(text[::6])            # сеикал
# text = text[2:9] + text[-5] + text[:2]

# Списки: введение
## list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)                  # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)                  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                    # [20, 4, 6, 8, 10]
# print(numbers)                  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)                                        # red green blue

# for e in colors:
#     print(e * 2)                                    # redred greengreen blueblue

# colors.append('grey')                               # добавить в конец
# print(colors == ['red', 'green', 'blue', 'grey'])   # True
# colors.remove('red')                                # del colors[0] удалить элемент

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 2
print(f(arg))
print(type(f(arg)))
