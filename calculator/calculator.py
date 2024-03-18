from tkinter import *
from tkinter.ttk import *

home = Tk()
home.geometry("615x330")
home.maxsize(615, 330)
home.minsize(615, 330)

row_ = 4
col_ = 0

def button_click(b):
    value.focus()
    value.insert(END, b)


def calc(a):
    if a == "=":
        val = value.get()
        if val.find('x'):
            val = val.replace('x', '*')
        if val == "":
            value.insert(0, "error")
        else:
            result_ = eval(val)
            value.delete(0, END)
            value.insert(0, result_)
    elif a == "(":
        value.insert(END, '(')
    elif a == ")":
        value.insert(END, ')')
    elif a == "C":
        value.delete(0, END)


buttons = ["1","2","3","+","4","5","6","-","7","8","9","x",".","0","%","/"]

buttons_ = ['(',')','=','C']

title_ = Label(home, text="MyCalcuator", font=("Ariel", 20))
title_.grid(column=1, columnspan=2)

value = Entry(home)
value.grid(columnspan=4, ipadx=60, pady=10)

for button in buttons:
    Button(home, text=button, command=lambda b=button: button_click(b)).grid(row = row_, column= col_, ipadx=30, padx=10, pady=10)
    col_ += 1
    if col_ > 3:
        row_ += 1
        col_ = 0

col_ = 0
for buttonn in buttons_:
    Button(home, text=buttonn, command=lambda a=buttonn: calc(a)).grid(row=row_, column=col_, ipadx= 30, padx=10, pady=10)
    col_ += 1
    if col_ > 3:
        row_ += 1
        col_ = 0


home.mainloop()