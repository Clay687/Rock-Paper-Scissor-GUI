from tkinter import *
import random
from time import strftime
from typing import runtime_checkable
import win32gui , win32con
from tkinter.messagebox import showinfo

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)

root.geometry("450x320")
root.maxsize(450,320)
root.minsize(450,320)
root.iconbitmap('C:\\Users\\prince\\Desktop\\GUI\\Required files\\Rock.ico')
root.title("Rock Paper Scissor Game")

Label(root,text="Rock Paper Scissor",fg="blue",font="lucida 20 bold underline").pack(pady=20)

def rule_func():
    showinfo("Rule","The player who score 5 points\nearlier win's the match")

rule = Menu(root)
rule.add_command(label="Rule",command=rule_func)
root.config(menu=rule)

computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

p_score = 0
c_score = 0

frame1 = Frame(root)
frame1.pack()

l1 = Label(frame1,text="Player",font="lucida 15")
l1.pack(side=LEFT)

l2 = Label(frame1,text="  VS  ",font="lucida 15")
l2.pack(side=LEFT)

l3 = Label(frame1,text="Computer",font="lucida 15")
l3.pack()

frame2 = Frame(root)
frame2.pack()

l4 = Label(frame2,text="",font="lucida 15",bg="white",borderwidth=2,relief="solid",width=15)
l4.pack(pady=10)

def reset_game():
    btn1["state"] = "active"
    btn2["state"] = "active"
    btn3["state"] = "active"
    l1.config(text = "Player")
    l3.config(text = "Computer")
    l4.config(text = "")

def button_disable():
    btn1["state"] = "disable"
    btn2["state"] = "disable"
    btn3["state"] = "disable"

def rock():
    global p_score,c_score
    if p_score==5:
        showinfo("Congrats","Player has won the match")
        p_score = 0
        c_score = 0
    elif c_score==5:
        showinfo("Lossed","Player has lossed the match")
        p_score = 0
        c_score = 0

    else:
        computer = computer_value[str(random.randint(0,2))]
        if computer=="Rock":
            result = "It's Draw"
        elif computer=="Paper":
            c_score +=1
            result = "Player Lose"
        elif computer=="Scissor":
            p_score +=1
            result = "Player Win"

        l4.config(text=result)
        p_lbl.config(text=p_score)
        c_lbl.config(text=c_score)
        l1.config(text="Rock")
        l3.config(text=computer)
        button_disable()


def scissor():
    global p_score,c_score
    if p_score==5:
        showinfo("Congrats","Player has won the match")
        p_score = 0
        c_score = 0
    elif c_score==5:
        showinfo("Lossed","Player has lossed the match")
        p_score = 0
        c_score = 0
    else:
        computer = computer_value[str(random.randint(0,2))]
        if computer=="Rock":
            c_score +=1
            result = "Player Lose"
        elif computer=="Paper":
            p_score +=1
            result = "Player Win"
        elif computer=="Scissor":
            result = "It's Draw"

        l4.config(text=result)
        p_lbl.config(text=p_score)
        c_lbl.config(text=c_score)
        l1.config(text="Scissor")
        l3.config(text=computer)
        button_disable()

def paper():
    global p_score,c_score
    if p_score==5:
        showinfo("Congrats","Player has won the match")
        p_score = 0
        c_score = 0
    elif c_score==5:
        showinfo("Lossed","Player has lossed the match")
        p_score = 0
        c_score = 0
    else:
        computer = computer_value[str(random.randint(0,2))]
        if computer=="Rock":
            p_score +=1
            result = "Player Win"
        elif computer=="Paper":
            result = "It's Draw"
        elif computer=="Scissor":
            c_score +=1
            result = "Player Lose"

        l4.config(text=result)
        p_lbl.config(text=p_score)
        c_lbl.config(text=c_score)
        l1.config(text="Paper")
        l3.config(text=computer)
        button_disable()

btn1 = Button(frame2,text="Rock",font="lucida 15",width=7,command=rock)
btn1.pack(side=LEFT,padx=10,pady=10)

btn2 = Button(frame2,text="Paper",font="lucida 15",width=7,command=paper)
btn2.pack(side=LEFT,padx=10,pady=10)

btn3 = Button(frame2,text="Scissor",font="lucida 15",width=9,command=scissor)
btn3.pack(side=LEFT,padx=10,pady=10)

frame3 = Frame(root)
frame3.pack()

reset_btn = Button(frame3,text="Reset Game",font="lucida 15",width=12,bg="red",command=reset_game)
reset_btn.pack()

palyer_score = Label(root,text="Player Score : ",fg="black",font="lucida 12")
palyer_score.place(x=20,y=280)

p_lbl = Label(root,text="0",font="lucida 12",bg="white",borderwidth=2,relief="solid",width=5)
p_lbl.place(x=130,y=280)

computer_score = Label(root,text="Computer Score : ",fg="black",font="lucida 12")
computer_score.place(x=260,y=280)

c_lbl = Label(root,text="0",font="lucida 12",bg="white",borderwidth=2,relief="solid",width=5)
c_lbl.place(x=390,y=280)

root.mainloop()