Nao = False
m1 = 1
media = 0
n = int(input("Digite um número inteiro: "))
op = str(input("Você dejesa continuar?[S/N] ")).upper()
soma = maior = menor = n

while not Nao:

    n = int(input("Digite um número inteiro: "))
    op = str(input("Você dejesa continuar?[S/N] ")).upper()
    m1 += 1
    soma += n

    if op == "N":

        if n > maior:
            maior = n
        elif menor < maior:
            menor = maior
        Nao = True

media = soma / m1
print(f"Você digitou {m1} números e a média foi {media:.2f}\nO MAIOR valor é {maior}")
print(f"O MENOR valor é {menor}")
