n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print(f"PARABÉNS VOCÊ FOI APROVADO\nSua média foi {media}")

elif media >= 5 or media <= 6.9:
    print(f"VOCÊ FICOU DE RECUPERAÇÃO\nSua média foi {media}")

else:
    print(f"VOCÊ FOI REPROVADO\nSua média foi {media}")