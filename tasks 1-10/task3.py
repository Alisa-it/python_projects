#  3.  Определение високосного года
from calendar import monthrange
#   Вариант 1
yearr = input("Введи год: ")
days = monthrange(int(yearr), 2)[1]
if days == 29:
    print("Это високосный год")
else:
    print("Это не високосный год")
#   Вариант 2
if int(yearr) % 4 == 0:
    print("Високосный")
else:
    print("Не високосный")