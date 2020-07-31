from tkinter import *

root=Tk()
root.title("Simple Calculator")

n = Entry(root, width = 80, borderwidth = 5)
n.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 12)

def button_click(num):
    current = n.get()
    n.delete(0,END)
    first = str(current) + str(num)
    n.insert(0,first)

def button_clearit():
    n.delete(0,END)
  
def button_addit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def button_subit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def button_multiplyit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def button_divideit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def button_modit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def gcd(a,b):
    if a>b:
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    elif b>a:
        if a == 0:
            return b
        else:
            return gcd(a,b%a)
    else:
        return a

def lcm(a,b):
    if a>b:
        bigger = a
        while True:
            if (bigger % a) == 0 and (bigger % b) == 0:
                return bigger
            bigger +=1
    elif b>a:
        bigger = b
        while True:
            if (bigger % a) == 0 and (bigger % b) == 0:
                return bigger
            bigger +=1
    else:
        return a

def gcdit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def lcmit(sign):
    global first_num
    global s
    s = sign
    first_num = int(n.get())
    n.delete(0,END)

def button_equalit():
    second_num = int(n.get())
    n.delete(0,END)
    if s == '+':
        ans = first_num + second_num
    elif s == '-':
        ans = first_num - second_num
    elif s == '*':
        ans = first_num * second_num
    elif s == '/':
        ans = first_num/second_num
        if ans == int(ans):
            ans = int(ans)
    elif s == '%':
        ans = first_num % second_num
    elif s == 'gcd':
        ans = gcd(first_num, second_num)
    elif s == 'lcm':
        ans = lcm(first_num, second_num)
    n.insert(0,ans)

button_1 = Button(root, width = 10, text="1", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(1))
button_1.grid(row = 1, column = 0)

button_2 = Button(root, width = 10, text="2", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(2))
button_2.grid(row = 1, column = 1)

button_3 = Button(root, width = 10, text="3", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(3))
button_3.grid(row = 1, column = 2)

button_4 = Button(root, width = 10, text="4", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(4))
button_4.grid(row = 1, column = 3)

button_5 = Button(root, width = 10, text="5", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(5))
button_5.grid(row = 2, column = 0)

button_6 = Button(root, width = 10, text="6", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(6))
button_6.grid(row = 2, column = 1)

button_7 = Button(root, width = 10, text="7", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(7))
button_7.grid(row = 2, column = 2)

button_8 = Button(root, width = 10, text="8", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(8))
button_8.grid(row = 2, column = 3)

button_9 = Button(root, width = 10, text="9", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(9))
button_9.grid(row = 3, column = 0)

button_0 = Button(root, width = 10, text="0", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_click(0))
button_0.grid(row = 3, column = 1)

button_clear = Button(root, width = 22, text="Clear", padx = 10, pady = 10, font=('Times new roman', '15'), command=button_clearit)
button_clear.grid(row = 3, column = 2, columnspan = 2)

button_add = Button(root, width = 10, text="➕", padx = 10, pady = 10, font=('Times new roman', '15 '), command=lambda: button_addit('+'))
button_add.grid(row = 4, column = 0)

button_subtract = Button(root, width = 10, text="➖", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_subit('-'))
button_subtract.grid(row = 4, column = 1)

button_multiply = Button(root, width = 10, text="✖", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_multiplyit('*'))
button_multiply.grid(row = 4, column = 2)

button_division = Button(root, width = 10, text="➗", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_divideit('/'))
button_division.grid(row = 4, column = 3)

button_mod = Button(root, width = 10, text="MOD", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: button_modit('%'))
button_mod.grid(row = 5, column = 0)

button_gcd = Button(root, width = 10, text="GCD", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: gcdit('gcd'))
button_gcd.grid(row = 5, column = 1)

button_lcm = Button(root, width = 10, text="LCM", padx = 10, pady = 10, font=('Times new roman', '15'), command=lambda: lcmit('lcm'))
button_lcm.grid(row = 5, column = 2)

button_equal = Button(root, width = 10, text="=", padx = 10, pady = 10, font=('Times new roman', '15'), command=button_equalit)
button_equal.grid(row = 5, column = 3)

root.mainloop()

