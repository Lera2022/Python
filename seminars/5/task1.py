# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнилось условие A[i] - 1 = A[i - 1]. Найдите это число.
# 1 2 3 4 6 7 8 9

# path = '1.txt'
# f = open(path, 'r')
# data = f.read().split()
# print(data)
# f.close()

# data = list(map(int, data))
# print(data)

# for i in range(len(data)-1):
#     if data[i] + 1 == data[i+1]:
#         continue
#     else:
#         print(data[i] + 1)

# a = [11, 12, 13, 14, 15, 17, 18, 21]
# res = [a[i]+1 for i in range(len(a)-1) if a[i + 1] - 1 != a[i]]
# print(res)

s = list(map(int, '11 12 13 15 16 17 18 19 20'. split()))
a = list(filter(lambda x: x[1]-x[0] == s[0], list(zip(range(len(s)), s))))
print(list(zip(range(len(s)), s)))
print(a)