import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

from tkinter import *
from tkinter.font import *


if __name__ == "__main__":
    root = Tk()
    
    root.title("the first GUI programming")
    root.geometry("300x300+100+200")
    root.resizable(True, False)
    
    fonts = families()
    """
    for font in fonts:
        print(font)
    """
    ft = Font(family='Nanum Gothic', size=12, weight='bold', slant='italic', underline=False)
    btn = Button(root, text="Button", width=30, height=10, padx=3, pady=3, 
                 background='yellow', foreground='black', 
                 font=ft, anchor='w', 
                 relief='raised', cursor='hand2')
    
    btn.pack()
    
    root.mainloop()