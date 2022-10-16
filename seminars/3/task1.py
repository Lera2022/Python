# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# from datetime import datetime

# def get_rand_int(num):
#     time = datetime.now()
#     rng = time.microsecond
#     return rng % num
# print(get_rand_int(100))

import datetime

dt = datetime.datetime.now()
result = round((dt.microsecond / dt.minute + 1) / dt.second)
print(f'Случайное число: {result}')