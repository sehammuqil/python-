from tkinter import *
from tkinter import messagebox
gamewindow=Tk()
gamewindow.title(" TIC-Tac-Toe ")
gamewindow.geometry("300x300") 

turn=1


def clicked1():
    global turn
    if btn1["text"]==" ":
        if turn==1:
            turn =2
            btn1["text"]="X"
        elif turn==2:
            turn=1
            btn1["text"]="O"
        check()
def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2
            btn2["text"]="X"
        elif turn==2:
            turn=1
            btn2["text"]="O"
        check()
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2
            btn3["text"]="X"
        elif turn==2:
            turn=1
            btn3["text"]="O"
        check()
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2
            btn4["text"]="X"
        elif turn==2:
            turn=1
            btn4["text"]="O"
        check()
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2
            btn5["text"]="X"
        elif turn==2:
            turn=1
            btn5["text"]="O"
        check()
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2
            btn6["text"]="X"
        elif turn==2:
            turn=1
            btn6["text"]="O"
        check()
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2
            btn7["text"]="X"
        elif turn==2:
            turn=1
            btn7["text"]="O"
        check()
def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2
            btn8["text"]="X"
        elif turn==2:
            turn=1
            btn8["text"]="O"
        check()
def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2
            btn9["text"]="X"
        elif turn==2:
            turn=1
            btn9["text"]="O"
        check()




btn1 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(gamewindow, text=" ",bg="gray", fg="Black",width=13,height=6,command=clicked9)
btn9.grid(column=3, row=3)

counter=1
def check():
    global counter
    counter=counter+1

    if btn1["text"]==btn2["text"]  and btn1["text"]==btn3["text"] and btn1["text"]=="O" or btn1["text"]==btn2["text"] and btn1["text"]==btn3["text"] and btn1["text"]=="X":
        win(btn1["text"])
    if btn4["text"]==btn5["text"] and btn4["text"]==btn6["text"] and btn4["text"]=="O" or btn4["text"]==btn5["text"] and btn4["text"]==btn6["text"] and btn4["text"]=="X":
        win(btn4["text"])
    if btn7["text"]==btn8["text"] and btn7["text"]==btn9["text"] and btn7["text"]=="O" or btn7["text"]==btn8["text"] and btn7["text"]==btn9["text"] and btn7["text"]=="X":
        win(btn7["text"])
    if btn1["text"]==btn4["text"] and btn1["text"]==btn7["text"] and btn1["text"]=="O" or btn1["text"]==btn4["text"] and btn1["text"]==btn7["text"] and btn1["text"]=="X":
        win(btn1["text"])
    if btn2["text"]==btn5["text"] and btn2["text"]==btn8["text"] and btn2["text"]=="O" or btn2["text"]==btn5["text"] and btn2["text"]==btn8["text"] and btn2["text"]=="X":
        win(btn2["text"])
    if btn3["text"]==btn6["text"] and btn3["text"]==btn9["text"] and btn3["text"]=="O" or btn3["text"]==btn6["text"] and btn3["text"]==btn9["text"] and btn3["text"]=="X":
        win(btn3["text"])
    if btn1["text"]==btn5["text"] and btn1["text"]==btn9["text"] and btn1["text"]=="O" or btn1["text"]==btn5["text"] and btn1["text"]==btn9["text"] and btn1["text"]=="X":
        win(btn1["text"])
    if btn7["text"]==btn5["text"] and btn7["text"]==btn3["text"] and btn7["text"]=="O" or btn7["text"]==btn5["text"] and btn7["text"]==btn3["text"] and btn7["text"]=="X":
        win(btn7["text"])
    if counter ==10:
        messagebox.showinfo("game over","game over")
        playagain()


def win(player):
    ans = "Game finished " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    playagain()

def playagain():
    global counter
    answer = messagebox.askquestion("one more time!","Do you want to play again, type yes or no  ( y/n )")
    if answer == "y" or "Y":
          btn1["text"] =btn2["text"]= btn3["text"]= btn4["text"]= btn5["text"]=btn6["text"]= btn7["text"]=btn8["text"]=btn9["text"]= " "
          counter = 0
    else:
          gamewindow.destroy()




gamewindow.mainloop()

