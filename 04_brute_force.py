# Метод грубой силы
def is_simple_number(x):
    """Определяет, является ли число простым.
    х - целое положительное число
    Если простое, то возвращает True,
    а иначе - False
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor += 1
    return True

def factorize_number(x):
    """ Раскладывает число на множители.
    Печатает их на экран.
    :param x: целое положительное число
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

# print(is_simple_number(19))
factorize_number(5835741)