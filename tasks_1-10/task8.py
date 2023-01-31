#  8.  Разложение числа на произведение простых чисел с их степенями, если надо

value = int(input('введите число: '))
i = 2
els = []
while i * i <= value:
    while value % i == 0:
        els.append(i)
        value = value / i
    i = i + 1
if value > 1:
    els.append(int(value))
print(els)