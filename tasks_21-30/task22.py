#  22. Перевернуть строку

s = input('Введи строку, которую нужно перевернуть: ')
ar = [' '] * len(s)
for el in range(len(s)):
    ar[len(s) - el-1] = s[el]

print(''.join(ar))