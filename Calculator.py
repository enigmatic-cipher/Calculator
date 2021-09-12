from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("380x300")
root.minsize(380,300)
root.maxsize(380,300)

c = Entry(root, width=25, bd=5, font=('Times', 20))
c.grid(row=0, column=0, padx=4, pady=4, columnspan=10)


def num_click(number):
    new_number = c.get()
    c.delete(0, END)
    c.insert(0, str(new_number) + str(number))


def addition():
    first_number = c.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    c.delete(0, END)


def subtraction():
    first_number = c.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    c.delete(0, END)


def multiplication():
    first_number = c.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    c.delete(0, END)


def division():
    first_number = c.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    c.delete(0, END)


def clear():
    c.delete(0, END)


def equal():
    second_number = c.get()
    c.delete(0, END)

    if math == "add":
        c.insert(0, f_num + int(second_number))

    elif math == "sub":
        c.insert(0, f_num - int(second_number))

    elif math == "div":
        c.insert(0, f_num / int(second_number))

    elif math == "mul":
        c.insert(0, f_num * int(second_number))


figure_0 = Button(root, text="0", padx=40, pady=20, command=lambda: num_click(0))
figure_1 = Button(root, text="1", padx=40, pady=20, command=lambda: num_click(1))
figure_2 = Button(root, text="2", padx=40, pady=20, command=lambda: num_click(2))
figure_3 = Button(root, text="3", padx=40, pady=20, command=lambda: num_click(3))
figure_4 = Button(root, text="4", padx=40, pady=20, command=lambda: num_click(4))
figure_5 = Button(root, text="5", padx=40, pady=20, command=lambda: num_click(5))
figure_6 = Button(root, text="6", padx=40, pady=20, command=lambda: num_click(6))
figure_7 = Button(root, text="7", padx=40, pady=20, command=lambda: num_click(7))
figure_8 = Button(root, text="8", padx=40, pady=20, command=lambda: num_click(8))
figure_9 = Button(root, text="9", padx=40, pady=20, command=lambda: num_click(9))
figure_add = Button(root, text="+", padx=38.5, pady=20, command=addition)
figure_sub = Button(root, text="-", padx=40, pady=20, command=subtraction)
figure_mul = Button(root, text="*", padx=40, pady=20, command=multiplication)
figure_div = Button(root, text="/", padx=40, pady=20, command=division)
figure_clr = Button(root, text="Clear", padx=29.5, pady=20, command=clear)
figure_equal = Button(root, text="=", padx=40, pady=20, command=equal)


figure_0.grid(row=4, column=2)
figure_1.grid(row=3, column=1)
figure_2.grid(row=3, column=2)
figure_3.grid(row=3, column=3)
figure_4.grid(row=2, column=1)
figure_5.grid(row=2, column=2)
figure_6.grid(row=2, column=3)
figure_7.grid(row=1, column=1)
figure_8.grid(row=1, column=2)
figure_9.grid(row=1, column=3)
figure_add.grid(row=1, column=4)
figure_sub.grid(row=2, column=4)
figure_mul.grid(row=3, column=4)
figure_div.grid(row=4, column=4)
figure_clr.grid(row=4, column=1)
figure_equal.grid(row=4, column=3)

root.mainloop()
