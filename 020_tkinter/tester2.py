from tkinter import *

root = Tk()
root.title('Squares calculator')

root.geometry('640x480')
user_entry = Entry(root, width=35, borderwidth=5)
user_entry.grid(row=0, column=0, columnspan=3)

display_text = StringVar()
my_label = Label(root, textvariable=display_text)
my_label.grid(row=1, column=0)

def get_squares(number):
    display_text.set(int(number) ** 2)

my_button = Button(root, text='Count squares', command=lambda: get_squares(user_entry.get()))
my_button.grid(row=0, column=3)

root.mainloop()