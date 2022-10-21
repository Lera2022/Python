# Найдите корни квадратного уравнения Ax2 + Bx + C = 0 двумя способами: с помощью математических формул нахождения корней квадратного уравнения. Вводим из файла.

f = open('t2.txt', 'r')
str = f.readline()
print(str)
str2 = str.replace(' ', '')[:-2]
print(str2)

a = str2.split('x')[0]
print(a)

list = str2.replace('-', '+-').split('+')
print(list)

list2 = []
for i in range(len(list)):
    if list[i].find('x^2') != -1:
        a = int(list[i].replace('x^2', ''))
    else:
        list2.append(list[i])
print(list2)
for  i in range(len(list2)):
    if list2[i].find('x') != -1:
        b = int(list2[i].replace('x', ''))
    else:
        c = list2[i]
print(a)
print(b)
print(c)