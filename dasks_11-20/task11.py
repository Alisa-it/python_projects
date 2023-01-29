#  11. Перевод чисел из 2 в 10 и обратно
def convertation1(val, base):
    i = 0
    converted_val = 0
    length = len(val) - 1
    while length >= 0:
        converted_val += (int(val[i])*(base**length))
        length -= 1
        i += 1
    return converted_val


def convertation2(val, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while val > 0:
        result = digits[val % base] + result
        val //= base
    return result


value_in_duo = str(input("Введи число в двоичной системе (например 1010110): "))

print('В десятичной оно равно', convertation1(value_in_duo, 2))
value_in_ten1 = str(input("Теперь введи число в десятичной системе: "))
print(convertation2(int(value_in_ten1), 2))
