# Массивы
# Данные, хранящиеся в массиве имеют одинаковый тип

A = [1,2,3,4,5]
for x in A:
    print(x, type(x))
    x += 1
    print(x)

print(A)