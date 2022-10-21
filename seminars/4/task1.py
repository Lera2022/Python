# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# f = open('t1.txt', 'r')
# lst = f.readline()

row = []
f = open('t1.txt', 'r')
for line in f.readlines():
    for i in line.split(" "):
        row.append(i)

print(row)
f.close()

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
list = []

for i in range(len(row)):
    if is_float(row[i]):
        list.append(float(row[i]))

min = list[0]
max = list[0]

for i in range(len(list)):
    if list[i] < min:
        min = list[i]
    elif list[i] > max:
        max = list[i]

print(list)
print(f'min = {min}')
print(f'max = {max}')