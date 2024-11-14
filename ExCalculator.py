from tkinter import *
from math import sqrt

maincalculator = Tk()
maincalculator.title("Calculator")
maincalculator.geometry("400x450")
maincalculator.configure(bg="#1e1e1e")

def calculate(inputvalue):
    if inputvalue == "C":
        display_var.set("")
    elif inputvalue == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except:
            display_var.set("Error!!")
    elif inputvalue == "√":
        try:
            result = sqrt(float(display_var.get()))
            display_var.set(result)
        except:
            display_var.set("Error!!")
    else:
        display_var.set(display_var.get() + inputvalue) #เพิ่มค่าใหม่
display_var = StringVar()
diaplay = Entry(maincalculator,textvariable=display_var,font=('Arial',20),justify="right")
diaplay.grid(row=0,column=0,columnspan=4,sticky="nsew")

buttons = [
    ("√",1,0), (".",1,1), ("**",1,2), ("C",1,3),
    ("7",2,0), ("8",2,1), ("9",2,2), ("/",2,3),
    ("4",3,0), ("5",3,1), ("6",3,2), ("*",3,3),
    ("1",4,0), ("2",4,1), ("3",4,2), ("-",4,3),
    ("0",5,0), ("=",5,2), ("+",5,3)
]
for (text,row,column) in buttons:
    if text == "0":
        Button(maincalculator, text=text,font=('Arial',20),padx=30,pady=15,fg="black",command=lambda x=text:calculate(x)).grid(row=row,column=column,columnspan=2,sticky="nsew")
    else:
        Button(maincalculator, text=text,font=('Arial',20),padx=30,pady=15,fg="black",command=lambda x=text:calculate(x)).grid(row=row,column=column,sticky="nsew")
maincalculator.mainloop()
