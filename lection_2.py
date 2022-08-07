# # Хотя бы одно делится на 10
# isDiv = False
#
# N = int(input())
#
# for i in range (N):
#     x = int(input())
#     isDiv = (x % 10 == 0) or isDiv
#
# print(isDiv)
#
# # Все делятся на 10
# isDiv = True
#
# N = int(input())
#
# for i in range (N):
#     x = int(input())
#     isDiv = (x % 10 == 0) and isDiv
#
# print(isDiv)

# Делится на 2 и на 3
# x = int(input())
#
# if (x % 2 == 0):
#     print('y')
#
# if (x % 3 == 0):
#     print('y')

# Каскадные условия
i = int(input())

if (i < 0):
    print("A")
elif (i < 5):
    print("B")
elif (i <= 10):
    print("C")
else:
    print("D")