preco1 = menor = c = 0
preco2 = 0
con = 0
barato = ""


while True:
    print("-=" * 20)
    nome = str(input("Digite o nome do produto: "))
    preco = int(input("Digite o valor do produto: R$"))
    preco1 += preco
    preco2 = preco
    c += 1

    if c == 1 or preco < menor:
        menor = preco
        barato = nome

    if preco2 > 1000:
        con += 1

    fim = str(input("Você deseja continuar?[S/N] ")).upper().strip()[0]
    while fim != "S" and fim != "N":
        fim = str(input("Você deseja continuar?[S/N] ")).upper().strip()[0]
        print("-=" * 20)

    if fim == "N":
        print("-=" * 20)
        print(f"O produto mais barato foi o {barato} e o preço foi R${menor}")
        print(f"O total gasto foi R${preco1}")
        print(f"O total de produtos que custam mais de R$1000 foi {con}")
        print("-=" * 20)
        break
