import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Clock')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600,320)
root.configure(background= '#1D1D1D')

def get_hello():
    nome = os.getlogin()
    hello.config(text=f'Olá, {nome}@')
def get_date():
    data_atual =strftime('%a, %d %b %Y')
    date.config(text=data_atual)

hello = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Montserrat', 16))
hello.pack()

date = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Montserrat', 14))
date.pack(pady=2)


get_hello()
get_date()


root.mainloop()