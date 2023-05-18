from math import floor
s2 = 0
c2 = 0
s3 = 0
s = 0
cin = 0
s1 = 0
c1 = 0

print("=-" * 15)
print("           BANCO ND")
print("=-" * 15)

n = int(input("Qual valor você deseja sacar? "))
print("=-" * 15)

if n >= 50:
    s = floor(n / 50)
    cin = n % 50
    print(f"Total de {s} cédulas de R$50")

if cin >= 20 and n >= 20:
    s1 = floor(cin / 20)
    c1 = cin % 20
    print(f"Total de {s1} cédulas de R$20")

if c1 >= 10:
    s2 = floor(c1 / 10)
    c2 = c1 % 10
    print(f"Total de {s2} cédulas de R$10")

if c2 >= 1:
    s3 = floor(c2 / 1)
    c3 = c2 % 1
    print(f"Total de {s3} cédulas de R$1")

print("=-" * 15)
print("Obrigado por utilizar meu Banco!!\nTenha um Bom Dia e volte sempre!!!")