salario = float(input("Digite o valor do seu salário: R$"))

aumento1 = salario * 15/100
aumento2 = salario * 10/100

if salario<=1250.00:
    print(f"Seu salário de R${salario} com o aumento de 15% foi para R${salario + aumento1}")
else:
    print(f"Seu salário de R${salario} com o aumento de 10% foi para R${salario + aumento2}")