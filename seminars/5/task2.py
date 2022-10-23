# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 6, 7] и т. д.

list = [1, 5, 2, 3, 4, 6, 1, 7]

# new_list = [list[0]]
# num = list[0]
# for i in list:
#     if i == num + 1:
#         new_list.append(i)
#         num += 1

# print(new_list)

result_list = []
count = 0
for i in range(0, len(list)-1):
    tmp_list = [list[i]]
    for j in range(i+1, len(list)):
        if list[j] > tmp_list[-1]:
            tmp_list.append(list[j])
            count += 1
    result_list.append(tmp_list)

print(result_list)
