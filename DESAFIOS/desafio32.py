from datetime import date
ano1 = int(input("Digite algum ano para saber se ele é bissexto:"))

if ano1 == 0:
    ano1 = date.today().year
if ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0:
    print(f"O ano {ano1} que você digitou é BISSEXTO")
else:
    print(f"O ano {ano1} que você digitou não é BISSEXTO")