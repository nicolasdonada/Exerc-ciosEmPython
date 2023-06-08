#Treinando composição

#Associação = Usar / Agregação = Tem / Composição = É dono

class Cor:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class Caneta:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

# Criando objetos Cor e Caneta e usando composição para associar uma cor à caneta
cor_azul = Cor("Azul", "#0000FF")
minha_caneta = Caneta("Bic", cor_azul)

print(minha_caneta.marca)  # Saída: Bic
print(minha_caneta.cor.nome)  # Saída: Azul
print(minha_caneta.cor.codigo)  # Saída: #0000FF
