def array_search(A: list, N: int, x: int):
    """Осуществляет поиск числа x в массиве A
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента x в массиве A.
        Или -1, если такого элемента нет.
        Если в массиве несколько одинаковых элементов равных x,
        то вернуть индекс первого по счету.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


if __name__ == '__main__':
    pass
