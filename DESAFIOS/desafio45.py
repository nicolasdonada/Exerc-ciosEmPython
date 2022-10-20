from random import choice
import time

print("\033[0;33m=-=-=-=-= GAME JOKENPO =-=-=-=-=\033[m")

print('''Suas opções:
[1] PEDRA
[2] TESOURA
[3] PAPEL''')

opcao = int(input("Qual sua opção? "))

lista = ["PEDRA","TESOURA","PAPEL"]
jogo = choice(lista)

time.sleep(1)
print("\033[0;31mJO\033[m")
time.sleep(1)
print("\033[0;32mKEN\033[m")
time.sleep(1)
print("\033[0;34mPO!!!\033[m")

if opcao == 1:

    if opcao != jogo and jogo == "TESOURA" and jogo != "PAPEL":
        print(f"=-=-=-=-= VOCÊ GANHOU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PEDRA =-=-=")

    elif opcao != jogo and jogo != "TESOURA" and jogo == "PAPEL":
        print(f"=-=-=-=-= VOCÊ PERDEU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PEDRA =-=-=")

    else:
         print(f"=-=-=-=-= DEU EMPATE!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PEDRA =-=-=")
         
elif opcao == 2:
    
    if opcao != jogo and jogo != "PEDRA" and jogo == "PAPEL":
        print(f"=-=-=-=-= VOCÊ GANHOU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU TESOURA =-=-=")
    
    elif opcao != jogo and jogo == "PEDRA" and jogo != "PAPEL":
        print(f"=-=-=-=-= VOCÊ PERDEU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU TESOURA =-=-=")

    else:
         print(f"=-=-=-=-= DEU EMPATE!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU TESOURA =-=-=")

elif opcao == 3:

    if opcao != jogo and jogo == "PEDRA" and jogo != "TESOURA":
        print(f"=-=-=-=-= VOCÊ GANHOU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PAPEL =-=-=")
    
    elif opcao != jogo and jogo != "PEDRA" and jogo == "TESOURA":
        print(f"=-=-=-=-= VOCÊ PERDEU!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PAPEL =-=-=")

    else:
        print(f"=-=-=-=-= DEU EMPATE!!! =-=-=-=-=\n=-=-= COMPUTADOR JOGOU {jogo} =-=-=\n=-=-= VOCÊ JOGOU PAPEL =-=-=")