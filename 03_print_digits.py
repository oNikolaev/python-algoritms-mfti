base = 10
x = int(input("Введите число: "))

while (x > 0):
    digit = x % base
    print(digit, end='')
    x //= base