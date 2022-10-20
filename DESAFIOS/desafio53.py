frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inver = junto[::-1]

print(f"O inverso de {junto} é {inver}")

if inver == junto:
    print("Temos um palíndromo!")

else:
    print("Não temos um palíndromo")