#  1.  Конвертер валют
def convert(a, s, f):
    return (s*a)/f


rate = {"рубль": 1, "доллар": 68.75, "евро": 74.69, "юань": 10.11}
convert_from = int(rate.get(input("{}\nКонвертируемая валюта: ".format(rate.keys()))))
convert_to = int(rate.get(input("Конвертируем в: ")))
summ = int(input("Сумма: "))
print("Результат: ", convert(convert_from, summ, convert_to))
