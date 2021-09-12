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


def reset():  # Resets the game
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL
    a = r.choice(['O', 'X'])


def check():  # Checks for victory or Draw
    global score1
    global score2
    for i in range(3):
        if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] \
                == b[2][i]["text"] == a:
            messagebox.showinfo("Congrats!!", "'" + name_entry1.get() + " ' has won")
            score1 += 1
            reset()
    if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] \
            == b[2][0]["text"] == a:
        messagebox.showinfo("Congrats!!", "'" + name_entry2.get() + "' has won")
        score2 += 1
        reset()
    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] \
            == b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED:
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()

