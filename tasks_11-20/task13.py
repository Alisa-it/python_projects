#  13. Факториал числа (с помощью циклов и рекурсии)

def factorial_iterative(num):  # цикл
    factorial = 1
    if num < 0:
        return "Факториал не вычисляется для отрицательных чисел"
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        return f"{num}! через цикл: {factorial}"


def factorial_recursive(num):  # рекурсия
    if num == 1:
        return num
    else:
        return num * factorial_recursive(num-1)


n = int(input('Введи число, для которого нужно вычислить факториал: '))

print(factorial_iterative(n), f'\n{n}! через рекурсию: {factorial_recursive(n)}')
