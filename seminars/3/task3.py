# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем "123", ответ -1
# - список: [], ищем "123", ответ: -1

def find_second_incl(text_list, substr):
    counter = 0
    while counter < len(text_list) and text_list[counter] != substr:
        counter += 1
    while counter < len(text_list) - 1:
        counter += 1
        if text_list[counter] == substr:
            return counter
    return -1
my_list = []
sub = "123"
pos = find_second_incl(my_list, sub)
if pos >= 0:
    print(f'подстрока {sub} второй раз встречается на позиции {pos}')
else:
    print(f'подстрока {sub} входит в список {my_list} менее 2 раз')