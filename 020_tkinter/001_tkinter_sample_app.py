# Sample Tkinter app
# * imports all classes from library
from tkinter import *

# This has to go first. It creates a window.
root = Tk()

# Title message on top of the app
root.title('This is sample app made by tkinter')

# Adding specific size to window
root.geometry('400x400')

# Creating a Label widget with text.
myLabel = Label(root, text="Hello world!")
myLabel.pack()


# This has to go last. It puts program into loop.
root.mainloop()