#  17. Гипотеза Коллаца

def kollatz(num):
    count = 0
    while num != 1:
        count += 1
        if num % 2 == 0:
            print(f'{count}) {int(num)}/2', end='=')
            num = num / 2
            print(int(num))
        else:
            print(f'{count}) ({int(num)}*3)+1', end='=')
            num = (num * 3) + 1
            print(int(num))

    return f'Потребовалось {count} шагов'


while True:
    num = int(input('Введи число: '))
    print(kollatz(num))