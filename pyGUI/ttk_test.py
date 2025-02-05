from tkinter import *
from tkinter.font import *
import tkinter.ttk as ttk

root = Tk()
#root.title = ("TTK Theme & Style")
root.title("TTK Theme & Style")
root.geometry("300x90+150+100")

style = ttk.Style()
theme_names = style.theme_names()
print(theme_names)
print(f"Default thems: {style.theme_use()}")

if len(theme_names) > 1:
	style.theme_use(theme_names[1])

#root.title(f"[ {style.theme_use()} ]")

fontH = Font(family="Helvetica", size=15, weight="bold")
style.configure(style=".", font=fontH)
#style.configure(style="Btn.TButton", foreground="blue", background="red")
style.configure(style="Btn.TButton", foreground="blue")

f1 = Frame(root, padx=5, pady=5)
f1.pack(fill=BOTH, expand=True)
ttk.Button(f1, text="OK").grid(row=0, column=0, sticky=E+W)
ttk.Button(f1, text="CANCEL", style="Btn.TButton").grid(row=1, column=0, sticky=E+W)
#ttk.Button(f1, text="OK").pack(fill=BOTH, expand=True)
#ttk.Button(f1, text="CANCEL", style="Btn.TButton").pack(fill=BOTH, expand=True)

f2 = Frame(root, padx=5, pady=5)
f2.pack(fill=BOTH, expand=True)
ttk.Checkbutton(f2, text="OK").grid(row=0, column=0, sticky=E+W)
ttk.Checkbutton(f2, text="CANCEL", style="Btn.TButton").grid(row=1, column=0, sticky=E+W)

f3 = Frame(root, padx=5, pady=5)
f3.pack(fill=BOTH, expand=True)
ttk.Radiobutton(f3, text="OK").grid(row=0, column=0, sticky=E+W)
ttk.Radiobutton(f3, text="CANCEL", style="Btn.TButton").grid(row=1, column=0, sticky=E+W)

root.mainloop()
