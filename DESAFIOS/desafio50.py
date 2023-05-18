soma = 0
cont = 0

for n in range(1, 7,):
    num = int(input(f"Digite um valor {n}:"))

    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você indicou {cont} PARES e a soma é {soma}")
