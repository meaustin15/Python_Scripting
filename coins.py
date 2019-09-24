import math
from tkinter import *

def num_coins(cents):
    coins = [25,10,5,1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += math.floor(cents / coin)
        cents = math.floor(cents % coin)
        if cents == 0:
            break
    return num_of_coins

def num_coins_gui(event):
    cents = int(change.get())
    coins = [25,10,5,1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += math.floor(cents / coin)
        cents = math.floor(cents % coin)
        if cents == 0:
            break
    result.delete(0, "end")
    result.insert(0,num_of_coins)


#print(min(num_coins(31), num_coins_nn(31)))

root=Tk()
root.title("Coin Change")
Label(root, text="Coin Change").pack()
change = Entry(root)
change.pack(side=LEFT)


btn = Button(root, text="Coins you get back")
btn.bind("<Button-1>", num_coins_gui)
btn.pack(side=LEFT)

result = Entry(root)
result.pack(side=LEFT)

root.mainloop()