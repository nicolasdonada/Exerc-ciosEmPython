from math import factorial

num = int(input("Digite um valor para calcular seu fatorial: "))
con = num
n1 = factorial(num)

while con > 0:
    print(f"{con} x ", end="")
    con -= 1
