from datetime import date
ano = int(input("Ano de nascimento: "))

atual = date.today().year
idade = atual - ano
alistamento = ano + 18
atra = 18 - idade
print(f"Quem nasceu em {ano} tem {idade} anos de idade em 2022.")

if  idade == 18:
    print("Você deve ir IMEDIATAMENTE se alistar")

elif idade < 18:
    print(f"Ainda não esta na hora de se alistar, você ira se alistar em {atra} anos")

elif idade > 18:
    print(f"Você passou {idade - 18} anos do seu alistamento")
    print(f"Se você se alistou, seu alistamento foi em {ano + 18}.")
