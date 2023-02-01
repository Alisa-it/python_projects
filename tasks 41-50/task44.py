#  44. Создание викторины (вопросы из файла, сравнивает с правильными ответами из файла)
import codecs
import random
f = codecs.open('questions.txt', 'r', encoding="utf-8")
count = 0
strcount = 0
for s in f:
    strcount += 1
    if not"ответ:" in s:
        ans = input(f'{s}').lower()
    if not'Вопрос:' in s:
        if (ans in s.lower()) and (ans != '') and (len(ans) > 1):
            print('Верно!')
            count += 1
        else:
            print(f'На самом деле, {s}', end='')
f.close()
strcount = int(strcount/2)
if count >= (strcount/2):
    print(f'Отличная работа! Твой результат: {count} из {strcount}')
else:
    print(f'Твой результат: {count} из {strcount}! Это неплохой результат... для начала')