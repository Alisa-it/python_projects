#  10. Пользователь вводит стоимость и кол-во денег, прог рассчитывает сдачу и кол-во монет для нее
def count(diff, change, k):
    while diff - change >= 0:
        k += 1
        diff = diff - change
    return diff, k
price = int(input("Цена: "))
summ = int(input("Кол-во денег: "))
k = 0
if price > summ:
    print("Не хватает денег")
else:
    diff = summ - price
    diff, ten = count(diff, 10, k)
    diff, five = count(diff, 5, k)
    diff, three = count(diff, 3, k)
    diff, two = count(diff, 2, k)
    diff, one = count(diff, 1, k)
    print("Сдача:\n10р - {}шт\n5р - {}шт\n3р - {}шт\n2р - {}шт\n1р - {}шт".format(ten, five, three, two, one))
