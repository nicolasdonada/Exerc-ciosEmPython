#Treinando encapsulamento

class MinhaClasse:

    def __init__(self):
        self.__nome = "Nicolas"

    def __mostrar(self):
        print("Método privado")

pessoa = MinhaClasse()

print(pessoa._MinhaClasse__nome)
pessoa._MinhaClasse__mostrar()