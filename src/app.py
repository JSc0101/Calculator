"""Tkinter."""
from tkinter import *

root = Tk()
root.title("Calculator", )

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0


def get__numbers(n):
    """Obtener numbers."""
    global i
    display.insert(i, n)
    i += 1


def get__operator(operator):
    """Obtener Operator."""
    global i
    operator__length = len(operator)
    display.insert(i, operator)
    i += operator__length


def delete__display():
    """Delete numbers."""
    display.delete(0, END)


def undo():
    """Delete Undo."""
    display__state = display.get()
    if len(display__state):
        display__new__state = display__state[:-1]
        delete__display()
        display.insert(0, display__new__state)
    else:
        delete__display()
        display.insert(0, "Error")


# - Buttons
Button(root, text="1", command=lambda: get__numbers(1)).grid(
    row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda: get__numbers(2)).grid(
    row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda: get__numbers(3)).grid(
    row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda: get__numbers(4)).grid(
    row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda: get__numbers(5)).grid(
    row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda: get__numbers(6)).grid(
    row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda: get__numbers(7)).grid(
    row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda: get__numbers(8)).grid(
    row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda: get__numbers(9)).grid(
    row=4, column=2, sticky=W+E)


# - Buttonn Arimetics

Button(root, text="AC", command=lambda: delete__display()).grid(
    row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda: get__numbers(0)).grid(
    row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda: get__operator(
    "%")).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda: get__operator("+")
       ).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda: get__operator("-")
       ).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: get__operator("*")
       ).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: get__operator("/")
       ).grid(row=5, column=3, sticky=W+E)

# - Button Unicode

Button(root, text="→", command=lambda: undo()).grid(
    row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda: get__operator(
    "**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda: get__operator(
    "**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda: get__operator(
    "(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda: get__operator(
    ")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=").grid(row=5, column=4, sticky=W+E, columnspan=2)

# - ROOT UI
root.mainloop()
