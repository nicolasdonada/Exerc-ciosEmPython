class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def adicionar_lista(self, carro):
        self.carros.append(carro)
    
    def mostrar_lista(self):
        for carro in self.carros:
            print(carro.modelo)
        
class Carro:

    def __init__(self, modelo):
        self.modelo = modelo
