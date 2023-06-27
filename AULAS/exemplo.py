'''import os

cpu = os.cpu_count()
timecpu = os.getlogin()

print(cpu)
print(timecpu)

username = os.getlogin()
print("Nome de usuário: username")'''

from tkinter import *
from time import strftime

janela = Tk()
janela.title("Relógio")
janela.geometry("600x400")
janela.config(bg="black")

def horas():
    label_hora["text"] = strftime("%H:%M:%S")
    
    label_hora.after(1000, horas)

label_hora = Label(janela, bg="black", text="AAAAAAAAA", fg="red", font="Arial 30 bold")
label_hora.pack()

horas()

janela.mainloop()