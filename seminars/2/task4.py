# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negateve.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case.

print('Введите целое число n:', end=' ')
n = int(input())

# def countBits(n):
#     pass
# def countBits(n):
#     return bin(n).count("1")
# print(bin(n).count("1"))

b = ''
i = 0 

while n > 0:
    a = n % 2
    b = str(a) + b
    n = n // 2
    if a == 1:
        i +=1
print(b, i)