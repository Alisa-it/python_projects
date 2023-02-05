#  16. Симуляция подбрасывания монеты. Подсчет результатов и вывод, сколько раз выпал о или р
from tkinter import *
import random


def clicked():
    global coin, count_r, count_o
    rez = random.choice(coin)
    if rez == 'орёл':
        count_o += 1
    if rez == 'решка':
        count_r += 1

    lbl.configure(text=f"На монетке {rez}")
    lbl2.configure(text=f"решка выпала {count_r} раз(а)\nорёл выпал {count_o} раз(а)")
    btn.configure(text="Ещё раз")


window = Tk()
window.title("Цветочный магазин")
window.geometry('500x200')

coin = ['орёл', 'решка']
count_r = count_o = 0

lbl = Label(text='Нажми на кнопку, чтобы подкинуть монетку', font=('arial bold', 14), pady=20, padx=10)
lbl.pack()
lbl2 = Label(text='', font=('arial', 10), pady=10, padx=10)
lbl2.pack()

btn = Button(window, text="Подкинуть", bg='black', pady=10, padx=10, fg='white', command=clicked)
btn.pack()
window.mainloop()
