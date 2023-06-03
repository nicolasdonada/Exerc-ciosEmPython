#Treinando metodos de classes

class Carro:
    total_carros = 0

    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

        Carro.total_carros += 1
    
    def info_carros(self):
        print(f"Modelo: {self.modelo}\nMarca: {self.marca}\n")

    @classmethod
    def carros_total(cls):
        print(f"Total: {cls.total_carros}")

carro1 = Carro("Fiesta", "Ford")
carro2 = Carro("Cruze", "Chevrolet")

carro1.info_carros()
carro2.info_carros()
Carro.carros_total()
