a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

def sum_interval(a, b):

    total = (a + b) * (b - a + 1) // 2
    print("Рассчеты сложения чисел с диапазона: ", total)

sum_interval(a, b)