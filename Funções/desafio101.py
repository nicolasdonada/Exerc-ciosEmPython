from datetime import date

def vota(ano):
    ano2 = date.today().year
    idade = ano2 - ano

    print(f"Sua idade: {idade} anos")

    if idade >= 18 and idade <= 65:
        print("O voto é: OBRIGATÓRIO!")

    if idade >= 16 and idade <= 17 and idade > 65:
        print("O voto é: OPCIONAL!")

    if idade < 16:
        print("O voto é: NÃO VOTA!")

ano1 = int(input("Ano de nascimento: "))
vota(ano1)