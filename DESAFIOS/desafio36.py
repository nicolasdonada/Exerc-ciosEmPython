casa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o valor do seu salário: R$"))
anos = int(input("Em quantos anos você prentende pagar:"))

sala = salario * 30/100
ano = casa / (anos * 12)

if salario <= sala:
    print(f"PARABÉNS SEU EMPRÉSTIMO FOI APROVADO!!\nVocê tera que pagar uma prestação de R${ano:.2f}")
    
else:
    print(f"Para pagar um casa de R${casa:.2f} durante {anos} anos você teria que pagar uma prestação de R${ano:.2f}\nEmpréstimo NEGADO!!")