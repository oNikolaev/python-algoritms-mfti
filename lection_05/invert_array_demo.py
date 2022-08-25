def invert_array(A: list, N: int):
    """Обращение массива (поворот задом-наперед) в рамках индексов от 0 до N-1"""
    for k in range(N//2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    actual = invert_array(A, 5)
