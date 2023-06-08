from classes import Escritor
from classes import Caneta

autor =  Escritor("Tolkien")
caneta = Caneta("Bic")
Escritor.ferramenta = caneta


caneta.escrever()
Escritor.ferramenta.escrever()
print(caneta.marca)
