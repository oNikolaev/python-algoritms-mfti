print("Hello world!")

x = "Hello world!"
print(x)

print(type(x))

x = 1 + 2 + 3 * 2
print(x)

a = 5
b = 2
print(a, b)

tmp = a
a = b
b = tmp
print(a, b)

a, b = b, a
print(a, b)

x, y, z = 1, 2, 3
print(x, y, z)

print(x ** y)
print(3 ** 0.5)

print(x//y)

print(x%y)

print(-11 // 10)
print(-11 % 10)

print("while")
a = 10
while a >= 0:
    print(a)
    a -= 1
else:
    print(a)

print("break")
a = 10
while a >= 0:
    print(a)
    a -= 1
    if (a == 5):
        break
else:
    print("else")
    print(a)

x = int(input())

print("nested loops")
while x > 0:
    y = x
    while y > 0:
        print(y)
        y -= 1
    x -= 1

print("for loop")
for x in 2, 5, 4, 3:
    print(x ** 2)

print("for loop range")
for x in range(1, 10, 1):
    print(x)
