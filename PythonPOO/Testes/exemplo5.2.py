class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade

    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        self._idade = idade

p1 = Pessoa("Luiz", 10)

print(f"Nome: {p1.get_nome()}\nIdade: {p1.get_idade()}")

p1.set_nome("João")
p1.set_idade(23)

print(f"Nome: {p1.get_nome()}\nIdade: {p1.get_idade()}")