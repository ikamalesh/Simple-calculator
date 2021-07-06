from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("235x400")
root.iconbitmap("maths.ico")
root.configure(bg="floral white")
entry = Entry(root, width=18, borderwidth=7, font="timesnewroman", bg="skyblue", fg="black")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=16)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_plus():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    entry.delete(0, END)


def button_minus():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)


def button_square():
    first_number = entry.get()
    global f_num
    global math
    math = "square"
    f_num = float(first_number)
    entry.delete(0, END)


def button_root():
    first_number = entry.get()
    global math
    global f_num
    math = "root"
    f_num = float(first_number)
    entry.delete(0, END)


def button_percent():
    first_number = entry.get()
    global math
    global f_num
    math = "percent"
    f_num = float(first_number)
    entry.delete(0, END)
    entry.insert(0, f_num / 100)


def button_equal():
    if math == "addition":
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, f_num / float(second_number))
    elif math == "square":
        second_number = entry.get()
        entry.delete(0, END)
        entry.insert(0, f_num ** float(second_number))


button_1 = Button(root, text="1", height=3, width=7, bg="pink", command=lambda: button_click(1))
button_2 = Button(root, text="2", height=3, width=7, bg="pink", command=lambda: button_click(2))
button_3 = Button(root, text="3", height=3, width=7, bg="pink", command=lambda: button_click(3))
button_4 = Button(root, text="4",height=3, width=7, bg="pink", command=lambda: button_click(4))
button_5 = Button(root, text="5", height=3, width=7, bg="pink", command=lambda: button_click(5))
button_6 = Button(root, text="6", height=3, width=7, bg="pink", command=lambda: button_click(6))
button_7 = Button(root, text="7", height=3, width=7, bg="pink", command=lambda: button_click(7))
button_8 = Button(root, text="8", height=3, width=7, bg="pink", command=lambda: button_click(8))
button_9 = Button(root, text="9", height=3, width=7, bg="pink", command=lambda: button_click(9))
button_0 = Button(root, text="0", height=3, width=7, bg="pink", command=lambda: button_click(0))
button_dot = Button(root, text=".", height=3, width=7, bg="pink", command=lambda: button_click("."))
button_clear = Button(root, text="Clear", height=3, width=7, bg="mediumorchid1", command=button_clear)
button_equals = Button(root, text="=", height=3, width=7, bg="light sky blue1", command=lambda: button_equal())

button_add = Button(root, text="+", height=3, width=7, bg="light green", command=button_plus)
button_minus = Button(root, text="-", height=3, width=7, bg="light green", command=button_minus)
button_multiply = Button(root, text="x", height=3, width=7, bg="light green", command=button_multiply)
button_divide = Button(root, text="/", height=3, width=7, bg="light green", command=button_divide)

button_percent = Button(root, text="%", height=3, width=7, command=button_percent)
button_square = Button(root, text="^", height=3, width=7, command=button_square)

button_quit = Button(root, text="Quit", height=3, width=7, bg="light coral", command=root.quit)

label = Label(root, text="About Version 1.0 ", bg="floral white", pady=20, justify=CENTER, fg='red')
# _______________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)

button_equals.grid(row=5, column=2)
button_clear.grid(row=1, column=2)

button_add.grid(row=5, column=3)
button_minus.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)

button_percent.grid(row=1, column=0)
button_square.grid(row=1, column=1)
button_quit.grid(row=1, column=3)
label.grid(row=6, column=0, columnspan=4)

root.mainloop()
