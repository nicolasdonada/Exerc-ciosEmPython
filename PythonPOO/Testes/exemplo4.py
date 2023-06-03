#Treinando Atributos de Classe

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

        Pessoa.total_pessoas += 1
    
    def mostrar_pessoas(self):
        print("Informações:")
        print(f"Nome: {self.nome}\nIdade: {self.idade}\n")

    @classmethod
    def imprimir_total(cls):
        print(f"Total de pessoas: {cls.total_pessoas}")


for n in range(1,6):
    p = Pessoa(input("Nome: "), 20)
    p.mostrar_pessoas()

Pessoa.imprimir_total()