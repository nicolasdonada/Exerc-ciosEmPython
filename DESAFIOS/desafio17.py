import math 

num = float(input("Digite o valor do cateto oposto: "))
num2 = float(input("Digite o valor do cateto adjacente: "))

po = math.pow(num, 2)
po2 = math.pow(num2, 2)
soma = float(po + po2)

print(f"Se o cateto oposto é {num} e o cateto adjacente é {num2} a hipotenusa vai ser {math.sqrt(soma):.2f}")

'''
from math import hypot 

num = float(input("Digite o valor do cateto oposto: "))
num2 = float(input("Digite o valor do cateto adjacente: "))

po = math.hypot(num, num2)

print(f"Se o cateto oposto é {num} e o cateto adjacente é {num2} a hipotenusa vai ser {po:.2f}")
'''
