# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Niyo Lynate')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tkinter import *
from tkinter import colorchooser #submodule

def click():
  color = colorchooser.askcolor()
  window.config(bg=color[1]) #change background color

window = Tk()
window.geometry("420x420")
button = Button(text='select color', command=click)
button.pack()
window.mainloop()

