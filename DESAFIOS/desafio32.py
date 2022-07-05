ano = int(input("Digite algum ano para saber se ele é bissexto:"))
ano1 = ano % 4

if ano1:
    print(f"O ano {ano} que você digitou não é BISSEXTO")
else:
    print(f"O ano {ano} que você digitou ele é BISSEXTO")