#  9.  Последовательно находить простое число
n = int(input("Введи кол-во: "))
k = 1
primes = 1
if n > 0:
    dec = [0] * n
    dec[0] = 1
    count = 0
while primes < n:
    for i in range(1, k):
        if (k == 2 or k == 3 or k == 5 or k == 7 or
            ((k % i == 0) and (k % (k**0.5) != 0) and (k % 2 != 0) and
             (k % 3 != 0) and (k % 5 != 0) and (k % 7 != 0))) and not(k in dec):
            count += 1
            dec[count] = k
            primes += 1
    k += 1
for i in dec:
    print(i, end=' ')