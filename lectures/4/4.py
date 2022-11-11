# 1
x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {x + y}')

# 2
def sum(a, b):
    return a + b

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x, y)}')

# 3
sum = lambda a, b: a + b

x = int(input('x = '))
y = int(input('y = '))
print(f'{x} + {y} = {sum(x, y)}')