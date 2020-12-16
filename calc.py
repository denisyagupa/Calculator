def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a/b


print("1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Возведение в степень")

choice = int(input())

if choice == 1:
    a = float(input())
    b = float(input())
    print(add(a, b))
elif choice == 2:
    a = float(input())
    b = float(input())
    print(minus(a, b))
elif choice == 3:
    a = float(input())
    b = float(input())
    print(mult(a, b))
elif choice == 4:
    a = float(input())
    b = float(input())
    print(div(a, b))
elif choice == 5:
    a = float(input())
    b = float(input())
    print(pow(a, b))
else:
    print("Ошибка ввода")


