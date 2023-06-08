from classes import Pessoa
from classes import Carro

pessoa1 = Pessoa("João")
carro1 = Carro("Ford")
carro2 = Carro("Chevrolet")



# Associação
pessoa1.adicionar_lista(carro1)
pessoa1.adicionar_lista(carro2)


# Listagem dos carros da pessoa
pessoa1.mostrar_lista()