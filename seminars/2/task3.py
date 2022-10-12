# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой

print('Введите строку 1:', end=' ')
string1 = input()
print('Введите строку 2:', end=' ')
string2 = input()

# count = string1.count(string2)

len_find_text = len(string1)
count = 0
for i in range (len(string2)):
    if string2[i: i + len_find_text] == string1:
        count += 1
print(count)