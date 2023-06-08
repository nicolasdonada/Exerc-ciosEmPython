#Treinando herança simples

class Pessoa:#Superclasse

    def __init__(self, nome, idade, estuda=False):
        self.estuda = estuda
        self.nome = nome
        self.idade = idade

    def estudar(self):
        self.estuda = True
        if self.estuda:
            print(f"{self.nome} está estudando...")

    def jogar(self):
        if self.estuda:
            print(f"{self.nome} não pode jogar está estudando...")
        
        else:
            print(f"{self.nome} está indo jogar...")

class Cliente(Pessoa):#Subclasses
    pass

class Aluno(Pessoa):#Subclasses
    pass

c1 = Cliente("Nicolas", 20)
print(c1.nome, c1.idade)
c1.jogar()

print()
a1 = Aluno("João", 19)
print(a1.nome, a1.idade)
a1.jogar()