#Treinando classes

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade, comida=False, fala=False):
        self.nome = nome
        self.comida = comida
        self.fala = fala
        self.idade = idade
    
    def comer(self, alimento):
        if self.comida:
            print(f"{self.nome} já esta comendo.")
            return

        if self.fala:
            print(f"{self.nome} não pode comer falando.")
            return

        print(f"{self.nome} está comendo {alimento}")
        self.comida = True

    def falar(self, assunto):
        print(f"{self.nome} esta falando sobre {assunto}")
        self.fala = True


    @classmethod
    def ano_nascimento(cls,nome,ano_de_nascimento):
        idade = cls.ano - ano_de_nascimento
        return cls(nome,idade)

p1 = Pessoa.ano_nascimento("Luiz", 2005)

print(p1.nome,p1.idade)
p1.falar("Python")
p1.comer("maçã")
