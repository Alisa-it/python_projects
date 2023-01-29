#  25. Счетчик гласных побуквенно
glasn = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count = [0] * len(glasn)
while True:
    s = input('Введи строку: ')

    for el in s:
        for i in range(len(glasn)):
            if el in glasn[i]:
                count[i] += 1

    for i in range(len(glasn)):
        if count[i] > 0:
            print(f'{glasn[i]} - {count[i]}')
            count[i] = 0