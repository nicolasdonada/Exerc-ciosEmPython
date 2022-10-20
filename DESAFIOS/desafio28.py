from random import choice

print("\033[1;34m=============================\n=============================\033[m")
print("\033[1;33mBEM VINDO AO JOGO DA ADIVINHAÇÃO 1.0v\033[m")
print("\033[1;33mDIGITE UM NÚMERO ENTRE 1 E 5\033[m")
print("\033[1;34m=============================\n=============================\033[m")

num = int(input("Digite o número:"))

lista = [1, 2, 3, 4, 5]
sorteio = choice(lista)

if num == sorteio:
    print("\033[32mPARABÉNS VOCÊ ACERTOU!!!!!!!!")
else:
    print("\033[1;31mVOCÊ ERROU!!!!!!")