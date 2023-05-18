id = 0
maiorid = 0 
nomevelho = ""
idademulher = 0

for p in range(1, 5):
    print(f"----- Informe os dados da {p}ª pessoa -----")
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()
    id += idade

    if p == 1 and sexo == "M":
        maiorid = idade
        nomevelho = nome
    else:
        if sexo == "M" and idade > maiorid:
            maiorid = idade
            nomevelho = nome

    if p == 1 and sexo == "F":
        idademulher += 1
    else:
        if sexo == "F" and idade < 20:
            idademulher += 1

if idademulher == 1:
    print(f"Ao todo a {idademulher} MULHER com menos de 20 anos")
else:
    print(f"Ao todo a {idademulher} MULHERES com menos de 20 anos")

print(f"A média de idade do grupo é {id / 4} anos")
print(f"O homem mais velho é o {nomevelho} com {maiorid} anos")
