# Файлы

# with open('file.txt', 'a') as data:
#   data.write('line 1111\n')
#   data.write('line 2222\n')

# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors)  # разделителей не будет
# data.write('LINE121\n')
# data.write('LINE131\n')
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close

# exit()

# Функции

# import hello as h

# print(h.f(1))     # Целое
# print(h.f(2.3))   # 23
# print(h.f(28))    # None

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError: new_string() missing 1 required positional argument: 'count'

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # !!!
# print(new_string(4))        # 12

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Кортежи

# t = ()
# print(type(t))      # <class 'tuple'>
# t = (1,)
# print(type(t))      # <class 'tuple'>
# t = (1)
# print(type(t))      # <class 'int'>
# t = (28, 9, 1990)
# print(type(t))      # <class 'tuple'>
# colors = ['red', 'green', 'blue']
# print(colors)       # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)            # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# # print(t[0])             # red
# # print(t[2])             # blue
# # # print(t[10])          # IndexError: tuple index out of range
# # print(t[-2])            # green
# # print(t[-200])          # IndexError: tuple index out of range

# for e in t:
#     print(e)              # red gren blue

# t[0] = 'black'            # TypeError: 'tuple' object does not support item assignment

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))        # r:red g:green b:blue

# a = (3, 4, 5)
# # print(a)
# # print(a[0])
# # a[0] = 12 # TypeError: 'tuple' object does not support item assignment

# for item in a:
#     print(item)

# Словари

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary['up'])     # ↑
# # dictionary['up'] = 'up'
# # print(dictionary['up'])
# # print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary['left']) # ←
# # типы ключей могут отличаться
# del dictionary['left']      # удаление элемента

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))

# # for v in dictionary:
#     print(dictionary[v])

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # <class 'set'>
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'gray', 'red', 'green', 'blue'}
# colors.remove('red')
# print(colors) # {'gray', 'blue', 'green'}
# # colors.remove('red')
# # print(colors) # KeyError: 'red'
# colors.discard('red')
# print(colors) # {'gray', 'blue', 'green'}
# colors.clear()
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# # b = {2, 5, 8, 13, 21}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # <class 'set'>
# print(type(b))  # <class 'set'>
# print(type(c))  # <class 'set'>
a = {1, 1, 1, 1, 1}
print(a)            # {1}
# c = a.copy()
# print(c) # {1, 2, 3, 5, 8}
# u = a.union(b)
# print(u) # {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)
# print(i) # {8, 2, 5}
# dl = a.difference(b)
# print(dl) # {1, 3}
# dr = b.difference(a)
# print(dr) # {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q) # {1, 21, 3, 13}

# s = frozenset(a)

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1 = [1, 2, 3, 4, 5]

# # print(list1.pop(2))
# # print(list1.insert(2, 11))
# print(list1.append(11))
# print(list1)
