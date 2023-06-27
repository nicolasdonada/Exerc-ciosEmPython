from tkinter import *
from time import strftime


class Relogio:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Relógio")
        self.janela.geometry("400x400")
        self.janela.resizable(width=False, height=False)


        self.label1 = Label(self.janela, width=20, height=3, text="", font="Numerial 20 bold")
        self.label1.pack(anchor="center", pady=10)
        self.iniciar_tempo()
    
        self.janela.mainloop()

    def iniciar_tempo(self):
        self.label1["text"] = strftime("%H:%M:%S")

        self.label1.after(1000, self.iniciar_tempo)
        
        
        
relogio = Relogio()
relogio1 = Relogio()