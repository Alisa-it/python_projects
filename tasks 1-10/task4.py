#  4.  Найти max и min элементы в массиве
import random
arr = []
for i in range(10):
    arr.append(random.randint(-10, 10))
print("Исходный массив: ", arr)

max = 0
min = 99
for elem in arr:
    if elem > max:
        max = elem
    if elem < min:
        min = elem
print("Максимальное число в списке: {}\nМинимальное число в списке: {}".format(max, min))