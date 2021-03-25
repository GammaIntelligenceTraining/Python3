from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Squares calculator')
root.geometry('640x480')

def show():
    my_label = Label(root, text=dropdown.get()).pack()

menu_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dropdown = StringVar()
dropdown.set('Mon')
# dropdown_menu = OptionMenu(root, dropdown, *menu_list)
dropdown_menu = OptionMenu(root, dropdown, 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
dropdown_menu.pack()

my_button = Button(root, text='Show selection', command=show).pack()

root.mainloop()