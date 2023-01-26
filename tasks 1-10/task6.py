#  6.  Найти число пи до n-ой цифры
from math import pi
num = str(pi)
length = []
a = int(input('Количество знаков после запятой: ')) + 2
i = 0
while i < a:
    length.append(num[i])
    i +=1
print("".join(length))