# Функции

def hello():
    print("Hello world!")

def hello_name(name:str = "World"):
    print("Hello, ", name)

def max2(x, y):
    if (x > y):
        return x
    return y

def max3(x, y, z):
    return max2(x, max2(y, z))

f = hello
f()

# Параметры по умолчанию
hello_name("Alice")
hello_name()

print(max2(34, 85))
print(max3(32, 84, 1))

# Утиная типизация
print(max3("кот", "котенок", "котеночек"))

# Именованные параметры
def hello_sep(name="World", separator="_"):
    print("Hello", name, sep=separator)

hello_sep(separator="***")

# Стек вызовов

# Структурное программирование