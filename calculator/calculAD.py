#imports#
import sys
import tkinter as tk
from tkinter import ttk


#init root#
root = tk.Tk()
root.title("Small Calculator")


#vars#
o = None
a = 0
b = 0
secFlag = False
logFlag = False
bModeFlag = False
ops = [
    [["+", "-", "*", "/"],
     ["and", "or", "nand", "nor"]],
    [["//", "%", "^", "nthroot"],
     ["xor", "xnor", "imply", "nimply"]]
]

#output#
Screen = ttk.Label(root, text=a)
Screen.grid(row=0,column=1)

#defs#
def updateButtons():
    pB.config(text=f(0))
    mB.config(text=f(1))
    tB.config(text=f(2))
    dB.config(text=f(3))
def numBut(n, r, c):
    ttk.Button(
        root,
        text=n,
        command=lambda: num(n)
    ).grid(row=r, column=c, sticky="nsew")
def num(n):
    global a, b
    if logFlag:
        n = bool(n)
    if not bModeFlag:
        a = n
    else:
        b = n
    Screen.config(text=n)
def second():
    global secFlag
    secFlag = not(secFlag)
    updateButtons()
def logic():
    global logFlag
    logFlag = not(logFlag)
    updateButtons()
def f(n):
    global secFlag
    global logFlag
    if secFlag:
        s = 1
    else:
        s = 0
    if logFlag:
        l = 1
    else:
        l = 0
    return ops[s][l][n]
def startB(n):
    global o, bModeFlag
    bModeFlag = True
    o = f(n)
def startA():
    global bModeFlag
    bModeFlag = False
def compute():
    global o, a, b, bModeFlag
    if o == "+":
        n = a+b
    elif o == "-":
        n = a-b
    elif o == "*":
        n = a*b
    elif o == "/":
        n = a/b
    elif o == "//":
        n = a//b
    elif o == "%":
        n = a%b
    elif o == "^":
        n = a**b
    elif o == "nthroot":
        n = "i cant code that lmbo"
    elif o == "and":
        n = a and b
    elif o == "nand":
        n = not(a and b)
    elif o == "or":
        n = a or b
    elif o == "xor":
        n = a ^ b
    elif o == "nor":
        n = not(a or b)
    elif o == "xnor":
        n = not(a ^ b)
    elif o == "imply":
        n = (not(a)) or b
    elif o == "nimply":
        n = not(not(a) or b)
    else:
        n = "hi"
    a = n
    b = 0
    o = None
    bModeFlag = False
    Screen.config(text=n)
    return n
def clear():
    global o, a, b, bModeFlag
    o = None
    a = 0
    b = 0
    bModeFlag = False
    Screen.config(text=0)

#centering#
windWidth = 500
windHeight = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - windWidth / 2)
center_y = int(screen_height/2 - windHeight / 2)
root.geometry(f'{windWidth}x{windHeight}+{center_x}+{center_y}')

#buttons#
for i in range(1, 10):
    numBut(i, 3 - (i - 1) // 3, (i - 1) % 3)

numBut(0, 4, 1)
ttk.Button(
    root,
    text="Exit",
    command=lambda: sys.exit(0)
).grid(row=4,column=0,sticky="nsew")
ttk.Button(
    root,
    text="=",
    command=lambda: compute()
).grid(row=4,column=2,sticky="nsew")
ttk.Button(
    root,
    text="Clear",
    command=lambda: clear()
).grid(row=6,column=1,sticky="nsew")
ttk.Button(
    root,
    text="2nd",
    command=lambda: second()
).grid(row=6,column=0,sticky="nsew")
ttk.Button(
    root,
    text="Logic",
    command=lambda: logic()
).grid(row=6,column=2,sticky="nsew")

pB = ttk.Button(
    root,
    text=f(0),
    command=lambda: startB(0)
)
pB.grid(row=1,column=3,sticky="nsew")
mB = ttk.Button(
    root,
    text=f(1),
    command=lambda: startB(1)
)
mB.grid(row=2,column=3,sticky="nsew")
tB = ttk.Button(
    root,
    text=f(2),
    command=lambda: startB(2)
)
tB.grid(row=3,column=3,sticky="nsew")
dB = ttk.Button(
    root,
    text=f(3),
    command=lambda: startB(3)
)
dB.grid(row=4,column=3,sticky="nsew")
ttk.Button(
    root,
    text="credits",
    command=lambda: print("Created by Kacob Jerby. linktr.ee/kacobjerby")
).grid(row=6,column=3,sticky="nsew")

root.mainloop()
