from random import shuffle
n1 = str(input("Digite um nome: "))
n2 = str(input("Digite outro nome: "))
n3 = str(input("Digite outro nome: "))
n4 = str(input("Digite outro nome: "))

lista = [n1, n2, n3, n4]

shuffle(lista)

print(f"A ordem de apresentação será:\n{lista}")