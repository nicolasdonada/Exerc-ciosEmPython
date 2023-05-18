from random import randint
from time import sleep

print("Gerando 5 valores: ", end="")
def sorteia():
    global lista

    lista = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]

    for n in lista:
        print(n, end=" ", flush=True)
        sleep(0.5)
    print("PRONTO!")

def somaPar():

    soma = 0
    if len(lista) >= 0:
        for n in lista:
            if n % 2 == 0:
                soma += n
    print(f"A soma entres os pares é {soma}.")

sorteia()
somaPar()