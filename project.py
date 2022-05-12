
from tkinter import *
import random

root.title("Put It In The Bag!")
root.geometry("400x400")

L1 = Label(root)
L2 = Label(root)

List = "BTS mug, clock, batteries, Ice cream, Bracelet, Jeans, Stationary, Bedsheets, Curtains, TV, Body lotion"
L1["text"] = "Items written down : " + str(List)

def Items_written():
    random_list = random.sample(range(0,11),1)
    L2["text"] = "Put " + str(random_list) + "In The bag!"

L1.place(relx = 0.5, rely = 0.6, anchor = CENTER)

btn = Button(root, text="What should you put in the bag?", command = Items_written(), bg = "purple", fg = "white" )

L2.place(relx=0.5, rely = 0.7, anchor = CENTER)

root.mainloop()    
