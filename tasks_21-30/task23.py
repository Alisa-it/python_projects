#  23. Шифр Цезаря код и декод
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
def crypt(msg, n):
    dmsg = ''
    for i in msg:
        for j in range(len(alphabet)):
            if alphabet[j] == i:
                u = j+n
                if u >= len(alphabet):
                    u = u - len(alphabet)
                dmsg = dmsg + alphabet[u]
        if i == ' ':
                dmsg = dmsg + ' '
    return dmsg


choice = int(input("Если хочешь зашифровать сообщение введи - 1\n"
                   "Расшифровать - 2\n= "))
if choice == 1:
    msg = str(input("Введи сообщение которое хочешь зашифровать - "))
    n = int(input("Введи сдвиг - "))
    print(crypt(msg, n))
if choice == 2:
    msg = str(input("Введи сообщение которое хочешь расшифровать - "))
    for i in range(1, len(alphabet)):
        print('сдвиг на {} - '.format(i), crypt(msg, i))
