nasci = int(input("Digite o ano do seu nascimento: "))

ano = 2022 - nasci

print(f"Sua idade é {ano} anos")
if ano <= 9:
    print("A sua categoria de acordo com usa idade é MIRIM")

elif ano > 9 and ano < 15:
    print("A sua categoria de acordo com usa idade é INFANTIL")

elif ano > 14 and ano < 18:
    print("A sua categoria de acordo com usa idade é JÚNIOR")

elif ano > 19 and ano < 24:
    print("A sua categoria de acordo com usa idade é SÊNIOR")

else:
    print("A sua categoria de acordo com usa idade é MASTER")


