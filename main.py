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

hello = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Montserrat', 16))
hello.pack()

get_hello()


root.mainloop()