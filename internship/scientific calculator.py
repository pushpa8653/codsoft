import tkinter as tk
import math

# define trig functions using degrees
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    return math.log10(x)

def sqrt(x):
    return math.sqrt(x)

def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=25, font=("Arial",18))
entry.grid(row=0, column=0, columnspan=5)

buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('(',4,2),(')',4,3),
('sin(',5,0),('cos(',5,1),('tan(',5,2),('+',5,3),
('log(',6,0),('sqrt(',6,1),('=',6,2)
]

for (text,row,col) in buttons:
    if text == "=":
        tk.Button(root,text=text,width=6,height=2,command=calculate).grid(row=row,column=col)
    else:
        tk.Button(root,text=text,width=6,height=2,
                  command=lambda t=text: press(t)).grid(row=row,column=col)

tk.Button(root,text="C",width=25,height=2,command=clear).grid(row=7,column=0,columnspan=4)

root.mainloop()
