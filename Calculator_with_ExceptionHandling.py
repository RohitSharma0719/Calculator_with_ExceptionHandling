import tkinter as tk
from tkinter import messagebox as msgbox
mainwindow=tk.Tk()
mainwindow.title("Calculator")

def add():
    try:
        first=first_value.get()
        second=secondvalue.get()
        if len(first) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        elif  len(second) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        else:
            first,second=int(first),int(second)
            result_label.config(text="Operation Result is:"+str( first + second ))
    except ValueError:
        msgbox.showinfo("Warning", "Enter Integers only.\n\nCharcters operation can't be performed.")


def sub():
    try:
        first = first_value.get()
        second = secondvalue.get()
        if len(first) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        elif  len(second) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        else:
            first, second = int(first), int(second)
            result_label.config(text="Operation Result is:" + str(first - second))
    except ValueError:
        msgbox.showinfo("Warning", "Enter Integers only.\n\nCharcters operation can't be performed.")
def multiply():
    try:
        first = first_value.get()
        second = secondvalue.get()
        if len(first) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        elif  len(second) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        else:
            first, second = int(first), int(second)
            result_label.config(text="Operation Result is:" + str(first * second))
    except ValueError:
        msgbox.showinfo("Warning", "Enter Integers only.\n\nCharcters operation can't be performed.")
def divide():
    try:
        first = first_value.get()
        second = secondvalue.get()
        if len(first) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        elif  len(second) == 0:
            msgbox.showinfo("Warning", "Fill both entries.")
        else:
            first, second = int(first), int(second)
            result_label.config(text="Operation Result is:" + str(first / second))
    except ValueError:
        msgbox.showinfo("Warning", "Enter Integers only.\n\nCharcters operation can't be performed.")
    except ZeroDivisionError:
        msgbox.showerror("ERROR", "Number can not be divided by zero.\n\nPlease fill second number with another value.")

headinhlabel=tk.Label(mainwindow,text='Enter first number',pady=(10))
headinhlabel.pack()
first_value=tk.Entry(mainwindow)
first_value.pack()
headinhlabel=tk.Label(mainwindow,text='Enter second number',pady=(10))
headinhlabel.pack()
secondvalue=tk.Entry(mainwindow)
secondvalue.pack()



headinhlabel=tk.Label(mainwindow,text='Operations')
headinhlabel.pack()
button=tk.Button(mainwindow,text='+',command=lambda :add())
button.pack()

button=tk.Button(mainwindow,text='-',command=lambda :sub())
button.pack()

button=tk.Button(mainwindow,text='*',command=lambda :multiply())
button.pack()

button=tk.Button(mainwindow,text='/',command=lambda :divide())
button.pack()

result_label=tk.Label(mainwindow,text='Operation Result is:')
result_label.pack()


mainwindow.mainloop()
