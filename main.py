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
    data_atual = strftime('%a, %d %b %Y')
    date.config(text=data_atual)
def get_hour():
    hora_atual = strftime('%H:%M:%S')
    hour.config(text=hora_atual)
    hour.after(1000, get_hour)

margem = tk.Canvas(root, width=600, height=60, bg='#1D1D1D', bd=0, highlightthickness=0, relief='ridge')
margem.pack()

hello = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Britannic', 16))
hello.pack()

date = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Britannic', 14))
date.pack(pady=2)

hour = Label(root, bg='#1D1D1D', fg='#8E27EA', font=('Britannic', 64, 'bold'))
hour.pack(pady=2)

get_hello()
get_date()
get_hour()

root.mainloop()