from random import randint

print("\033[1;34m=============================\n=============================\033[m")
print("\033[1;33mBEM VINDO AO JOGO DA ADIVINHAÇÃO 2.0v\033[m")
print("\033[1;33mDIGITE UM NÚMERO ENTRE 1 E 10\033[m")
print("\033[1;34m=============================\n=============================\033[m")

acertou = False
vezes = 0

sorteio = randint(1, 10)

while not acertou:
    num = int(input("Digite seu palpite: "))
    vezes += 1

    if num == sorteio:
        acertou = True
    
    else:
        if num > sorteio:
            print("Menos... Tente novamente")
        elif num < sorteio:
            print("Mais... Tente novamente")

print(f"PARABÉNS!!!\nVocê acertou em {vezes} tentativas")