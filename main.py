from tkinter import *
from tkinter import messagebox
import random as r

top = Tk()
top.geometry('336x415')
top.resizable(0, 0)
top.title("Login")
top.iconbitmap("login.ico")
top.configure(bg = "lightblue1")
bef = Label(top, text = 'BEFORE ENTERING THE GAME', font = ("Helvetica", 10, 'bold'),
            bg = "lightblue1", fg = "indianred2")
ore = Label(top, text = 'PLEASE MENTION ....', font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "indianred2")
bef.grid(row = 1, column = 1)
ore.grid(row = 2, column = 1)
name = Label(top, text = "Player 1:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
name.grid(row = 3, column = 0, pady = 10)
name_entry1 = Entry(top, width = 30)
name_entry1.grid(row = 3, column = 1, columnspan = 10, pady = 10)
name2 = Label(top, text = "Player 2:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
name2.grid(row = 4, column = 0)
name_entry2 = Entry(top, width = 30)
name_entry2.grid(row = 4, column = 1, columnspan = 20)
email = Label(top, text = "E-mail:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
email.grid(row = 5, column = 0)
password = Label(top, text = "Password:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
password.grid(row = 6, column = 0)
gender = Label(top, text = "Gender:", font = ("Helvetica", 10, 'bold'), bg = "lightblue1", fg = "dark orchid")
gender.grid(row = 7, column = 0)
name_entry1 = Entry(top, width = 30)
name_entry1.grid(row = 3, column = 1, columnspan = 10, pady = 10)
name_entry2 = Entry(top, width=30)
name_entry2.grid(row=4, column=1, columnspan = 10, pady = 10)
email_entry = Entry(top, width = 30)
email_entry.grid(row = 5, column = 1, columnspan = 10, pady = 10)
password_entry = Entry(top, width = 30, show ="*")
password_entry.grid(row = 6, column = 1, columnspan = 10, pady = 10)
var = IntVar()
r2 = Radiobutton(top, text = 'male', value = 1, variable = var, bg = "lavender", fg = "black")
r2.grid(row = 7, column = 1, ipady = 5)
r3 = Radiobutton(top, text = 'female', value = 2, variable = var, bg = "lavender", fg = "black")
r3.grid(row = 7, column = 2, ipady = 5)

score1 = 0
score2 = 0


def button(frame):  # Function to define a button
    b = Button(frame, padx = 1, bg = "alice blue", width = 3, text = "", font = ('arial', 40, 'bold'),
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
    try:
        for i in range(3):
            for j in range(3):
                b[i][j]["text"] = " "
                b[i][j]["state"] = NORMAL
        a = r.choice(['O', 'X'])
    except ReferenceError:
        print("restart the game")


def check():  # Checks for victory or Draw
    global score1
    global score2
    for i in range(3):
        if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] \
                == b[2][i]["text"] == a:
            messagebox.showinfo("Congrats!!", "'" + name_entry1.get() + " ' has won")
            score1 += 1
            with open("scoreboard.txt ", "a") as file_object:
                file_object.writelines(name_entry1.get()+" "+"score=" + str(score1) + "\n")

            reset()
    if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] \
            == b[2][0]["text"] == a:
        messagebox.showinfo("Congrats!!", "'" + name_entry2.get() + "' has won")
        score2 += 1
        with open("scoreboard.txt ", "a") as file_object:
            file_object.writelines(name_entry2.get()+" "+"score=" + str(score1) + "\n")

        reset()
    elif b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] \
            == b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED:
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()


def click(row, col):  # Next players turn
    b[row][col].config(text = a, state = DISABLED, disabledforeground = colour[a])
    check()
    change_a()
    label.config(text = a + " 's Chance", font = ("Helvetica", 10, 'bold'))


def main():  # Main Program
    root = Toplevel()  # Window defined
    root.title("Tic-Tac-Toe")
    root.geometry('336x415')
    root.configure(bg = "alice blue")
    root.resizable(0, 0)
    root.iconbitmap("icon.ico")
    global a
    global b
    global colour
    global label
    a = r.choice(['O', 'X'])  # Two operators defined
    colour = {'O': "gold", 'X': "lawn green"}
    b = [[], [], []]
    for i in range(3):
        for j in range(3):
            b[i].append(button(root))
            b[i][j].config(command = lambda row=i, col=j: click(row, col))
            b[i][j].grid(row = i, column = j)
    label = Label(root, text = a + "'s Chance", font = ('helvetica', 10, 'bold'), bg ="alice blue")
    label.grid(row = 3, column = 0, columnspan = 3)
    score_label = Label(root, text = name_entry1.get() + ' ' + 'SCORE:' + str(score1),
                        font = ('Helvetica', 12, 'bold'), bg ="alice blue")
    score_label.grid(row = 5, column = 0, columnspan = 3)
    score_label = Label(root, text = name_entry2.get() + ' ' + 'SCORE:' + str(score2),
                        font = ('Helvetica', 12, 'bold'), bg ="alice blue")
    score_label.grid(row = 6, column = 0, columnspan = 3)
    root.mainloop()


def link():  # save user information in file
    nam = name_entry1.get()
    nam2 = name_entry2.get()
    em = email_entry.get()
    pw = password_entry.get()
    with open("scoreboard.txt", "a") as file_object:
        file_object.writelines(["player1=" + nam + "\t", "player2=" + nam2 + "\t",
                                "email=" + em + "\t", "password=" + pw + "\n"])

s = Label(top, text = " ", bg = "lightblue1")
s.grid(row = 9)
s = Label(top, text = " ", bg = "lightblue1")
s.grid(row = 11)
game_page = Button(top, text = 'SAVE INFO', command = link, font = ("Helvetica", 10, 'bold'),
                   bg = "dark orchid", fg = "white")
game_page.grid(row = 10, column = 1)
game_page = Button(top, text = 'New Game', command = main, font = ("Helvetica", 10, 'bold'),
                   bg = "dark orchid", fg = "white")
game_page.grid(row = 12, column = 1, rowspan=5)

top.mainloop()
