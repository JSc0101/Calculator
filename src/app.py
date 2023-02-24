from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# - Buttons
Button(root, text="1").grid(row=2, colum=0)
Button(root, text="2").grid(row=2, colum=0)
Button(root, text="3").grid(row=2, colum=0)

Button(root, text="4").grid(row=2, colum=0)
Button(root, text="5").grid(row=2, colum=0)
Button(root, text="6").grid(row=2, colum=0)

Button(root, text="7").grid(row=2, colum=0)
Button(root, text="8").grid(row=2, colum=0)
Button(root, text="9").grid(row=2, colum=0)


root.mainloop()
