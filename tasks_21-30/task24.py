#  24. ananabay
msg = str(input("Введи сообщение которое хочешь зашифровать - "))

m = msg.split()
new = ''
for word in m:
    r = word[0]
    for i in range(1, len(word)):
        new = new + word[i]
    new += r + 'ay '
print(new)
