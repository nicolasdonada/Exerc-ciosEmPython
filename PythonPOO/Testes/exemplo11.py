#Treinando sobreposição de membros

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando...")

class Cliente(Pessoa):

    def falar(self):
        #super().falar()
        print("Estou falando sobre outra coisa...")
    pass

class Cliente_VP(Cliente):

    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f"{self.nome} {self.sobrenome} está falando sobre Python...")

    pass


c1 = Cliente_VP("João", 12, "Donada")
c1.falar()