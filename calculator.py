import tkinter as tk
from tkinter import *
from tkinter import Label,messagebox,Button,Entry
root=tk.Tk()
root.title("Simple Calculator")
root.config(bg='white')

eqn=""

def press(num):
    global eqn
    eqn=eqn+str(num)
    equation.set(eqn)

def equal():
    try:
        global eqn
        total=str(eval(eqn))
        equation.set(total)

        eqn=""
    except:
        equation.set("error")
        eqn=""
def sum():
    press("+")
def sub():
    press("-")
def div():
    press("/")
def mul():
    press("*")

def one():
    press(1)
def two():
    press(2)
def three():
    press(3)
def four():
    press(4)
def five():
    press(5)
def six():
    press(6)
def sev():
    press(7)
def eig():
    press(8)
def nine():
    press(9)
def zero():
    press(0)
def decimal():
    press(".")


frame = Frame(root)
frame.pack()

equation = StringVar()
display=Entry(frame,textvariable=equation)
display.grid(row=0,column=0,columnspan=4)
tk.Button(frame,text="9",command=nine,width=8,height=5).grid(row=1,column=0)
tk.Button(frame,text="8",command=eig,width=8,height=5).grid(row=1,column=1)
tk.Button(frame,text="7",command=sev,width=8,height=5).grid(row=1,column=2)
tk.Button(frame,text="6",command=six,width=8,height=5).grid(row=2,column=0)
tk.Button(frame,text="5",command=five,width=8,height=5).grid(row=2,column=1)
tk.Button(frame,text="4",command=four,width=8,height=5).grid(row=2,column=2)
tk.Button(frame,text="3",command=three,width=8,height=5).grid(row=3,column=0)
tk.Button(frame,text="2",command=two,width=8,height=5).grid(row=3,column=1)
tk.Button(frame,text="1",command=one,width=8,height=5).grid(row=3,column=2)
tk.Button(frame,text="0",command=zero,width=8,height=5).grid(row=4,column=1)
tk.Button(frame,text="/",command=div,width=8,height=5).grid(row=1,column=3)
tk.Button(frame,text="*",command=mul,width=8,height=5).grid(row=2,column=3)
tk.Button(frame,text="+",command=sum,width=8,height=5).grid(row=3,column=3)
tk.Button(frame,text="-",command=sub,width=8,height=5).grid(row=4,column=3)
tk.Button(frame,text=".",command=decimal,width=8,height=5).grid(row=4,column=0)
tk.Button(frame,text="=",command=equal,width=8,height=5).grid(row=4,column=2)

root.mainloop()
