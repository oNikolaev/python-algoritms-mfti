# Позволяет сортировать очень большое количество данных очень быстро.
# O(M) - требования к памяти, M-количество различных элементов
# Это однопроходный алгоритм (поиск максимума, расчет суммы и пр.).

# Частотный анализ входных данных

def counting_sort(A: list):
    len_A = len(A)
    F = [0] * len_A
    for i in range(0, len_A):
        F[A[i]] += 1

    A_sorted = []
    for i in range(0, len_A - 1):
        A_sorted += [i] * F[i]

    return A_sorted


if __name__ == '__main__':
    pass
