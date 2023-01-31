#  2.  Калькулятор
list_of_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
list_of_signs = ["+", "-", "/", "*", "="]


def calculate(num, sign, res):
    if sign == "+":
        return res + num
    if sign == "-":
        return res - num
    if sign == "*":
        return res * num
    if sign == "/" and num != 0:
        return res / num
    else:
        print('!ОШИБКА! деление на ноль')
    if sign == "=":
        return res


equation = input("Введите выражение: ") + "="
i = result = 0
number = ''
sign = "+"
for symbol in equation:
    if symbol in list_of_numbers:
        number += symbol
    elif symbol in list_of_signs:
        try:
            result = calculate(int(number), sign, result)
        except ValueError:
            print("!ОШИБКА! некорректный ввод")
        number = ''
        sign = symbol

print("=", result)