def matryoshka(n: int):
    if n < 1:
        print("Матрешечка")
    else:
        print("матрешка верх - ", n)
        matryoshka(n - 1)
        print("матрешка низ - ", n)


if __name__ == '__main__':
    matryoshka(5)