# Копирование массивов

N = int(input("Введите размер массивов: "))
A = [0]*N
B = [0]*N

for k in range(N):
    A[k] = int(input("Введите число: "))

# Копирование массива
for k in range(N):
    B[k] = A[k]

print(A)
print(B)

C = A
print(C)

A[0] = 777
print(C)

C = list(A)