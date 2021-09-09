from tkinter import *
from tkinter import messagebox
import random as r

top = Tk()
top.geometry('336x410')
top.resizable(0, 0)
top.configure(bg = "lightblue1")
bef = Label(top, text = 'BEFORE ENTERING THE GAME', font = ("Helvetica", 10, 'bold'),
            bg = "lightblue1",fg = "indianred2")
ore = Label(top, text = 'PLEASE MENTION ....', font = ("Helvetica", 10, 'bold'), bg = "lightblue1",fg = "indianred2")
bef.grid(row = 1, column = 1)
ore.grid(row = 2, column = 1)
name = Label(top, text = "Player 1 Name:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
name.grid(row = 3, column = 0)
name_entry1 = Entry(top, width = 30)
name_entry1.grid(row = 3, column = 1, columnspan = 10, pady = 10)
name2 = Label(top, text = "Player 2 Name:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
name2.grid(row = 4, column = 0)
name_entry2 = Entry(top, width = 30)
name_entry2.grid(row = 4, column = 1, columnspan = 20)

score1 = 0
score2 = 0


def button(frame):  # Function to define a button
    b = Button(frame, padx = 1, bg = "papaya whip", width = 3, text = "", font = ('arial', 40, 'bold'),
               relief = "sunken", bd = 5)
    return b


def change_a():  # Function to change the operand for the next player
    global a
    for i in ['O', 'X']:
        if not (i == a):
            a = i
            break
