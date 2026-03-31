import tkinter as tk

# Functions
def add():
    data = e1.get()
    nums = data.split("+")
    result = int(nums[0]) + int(nums[1])
    e1.delete(0, tk.END)
    e1.insert(0, result)

def sub():
    data = e1.get()
    nums = data.split("-")
    result = int(nums[0]) - int(nums[1])
    e1.delete(0, tk.END)
    e1.insert(0, result)

def mul():
    data = e1.get()
    nums = data.split("*")
    result = int(nums[0]) * int(nums[1])
    e1.delete(0, tk.END)
    e1.insert(0, result)

def div():
    data = e1.get()
    nums = data.split("/")
    result = int(nums[0]) / int(nums[1])
    e1.delete(0, tk.END)
    e1.insert(0, result)

# Window
x = tk.Tk()
x.title("Calculator")

# Entry
e1 = tk.Entry(x)
e1.grid(row=0, column=1)

# Buttons 

b1 = tk.Button(x, text="+", command=add)
b1.grid(row=9, column=1)

b2 = tk.Button(x, text="-", command=sub)
b2.grid(row=9, column=2)

b3 = tk.Button(x, text="*", command=mul)
b3.grid(row=9, column=3)

b4 = tk.Button(x, text="/", command=div)
b4.grid(row=9, column=4)

x.mainloop()
