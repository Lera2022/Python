# # Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

MyList = ['qwe23', 'yui', 'etyuh', 'uioo'] 

MyFile=open('file1.txt', 'w')
for element in MyList:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()

with open('file1.txt') as f:
    lines = [line.rstrip('\n') for line in open('file1.txt')]
print(lines)

print('Введите число:', end=' ')
num = input()

def find_number(lines, num):
    index = -1;
    for i in lines:
        if i.find(num) >= 0:
            return True

data = open('file1.txt', 'a')

if find_number(lines, num):
    data.write('num is in the list')
else:
    data.write("num isn't in the list")
data.close()

# def findNum():
#     for i in list:
#         if i.find(numstr):
#             return True

# len_list = open('file1.txt', 'r')
# list = []
# for l in len_list.readlines():
#     list = (l.split(' '))
# len_list.close()
# print(list)
# num = 78
# numstr = str(num)
# print(findNum())