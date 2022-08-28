def insertion_sort(A: list):
    """Сортировка списка A вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while (k > 0 and A[k] < A[k - 1]):
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def selection_sort(A: list):
    """Сортировка списка A выбором"""
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A: list):
    """Сортировка списка A методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


if __name__ == '__main__':
    pass
