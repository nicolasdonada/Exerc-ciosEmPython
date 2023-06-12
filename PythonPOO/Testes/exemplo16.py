#Chamando métodos de classes filhas.

class Biblioteca:
    def chama_metodo(self):
        self.metodo_interface()

class Interface(Biblioteca):
    def metodo_interface(self):
        print("Sou a Interface")

eu = Interface()

eu.chama_metodo()