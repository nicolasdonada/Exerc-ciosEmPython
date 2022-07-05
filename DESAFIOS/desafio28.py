from random import choice

print("=============================\n=============================")
print("BEM VINDO AO JOGO DA ADIVINHAÇÃO 1.0v")
print("DIGITE UM NÚMERO ENTRE 1 E 5")
print("=============================\n=============================")
num = int(input("Digite o número:"))

lista = [1, 2, 3, 4, 5]
sorteio = choice(lista)

if num == sorteio:
    print("PARABÉNS VOCÊ ACERTOU!!!!!!!!")
else:
    print("VOCÊ ERROU!!!!!!")