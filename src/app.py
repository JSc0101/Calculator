from tkinter import *

root = Tk()
root.title("Calculator", )

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# - Buttons
Button(root, text="1").grid(row=2, column=0, sticky=W+E)
Button(root, text="2").grid(row=2, column=1, sticky=W+E)
Button(root, text="3").grid(row=2, column=2, sticky=W+E)

Button(root, text="4").grid(row=3, column=0, sticky=W+E)
Button(root, text="5").grid(row=3, column=1, sticky=W+E)
Button(root, text="6").grid(row=3, column=2, sticky=W+E)

Button(root, text="7").grid(row=4, column=0, sticky=W+E)
Button(root, text="8").grid(row=4, column=1, sticky=W+E)
Button(root, text="9").grid(row=4, column=2, sticky=W+E)


# Buttonn Arimetics

Button(root, text="AC").grid(row=5, column=0, sticky=W+E)
Button(root, text="0").grid(row=5, column=1, sticky=W+E)
Button(root, text="%").grid(row=5, column=2, sticky=W+E)

Button(root, text="+").grid(row=2, column=3, sticky=W+E)
Button(root, text="-").grid(row=3, column=3, sticky=W+E)
Button(root, text="*").grid(row=4, column=3, sticky=W+E)
Button(root, text="/").grid(row=5, column=3, sticky=W+E)

root.mainloop()
