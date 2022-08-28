if __name__ == '__main__':
    A = [x ** 2 for x in range(10)]
    print(A)

    B = [x ** 2 for x in A if x % 2 == 0]
    print(B)

    C = [(0 if x < 0 else x ** 2) for x in A if x % 2 == 0]
    print(C)
