def shift_array(A: list, N: int, method: str):
    if method == 'l':
        tmp = A[0]
        for k in range(N - 1):
            A[k] = A[k + 1]
        A[N - 1] = tmp
    elif method == 'r':
        tmp = A[N - 1]
        for k in range(N - 2, -1, -1):
            A[k + 1] = A[k]
        A[0] = tmp


if __name__ == '__main__':
    pass
