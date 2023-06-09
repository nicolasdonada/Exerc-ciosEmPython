#Treinando classes abstratas

#Classes abstratas são basicamente classes feitas para serem herdadas.

#Métodos abstratos são basicamente métodos que ficam dentro das classes abstratas mas que so serão implementados nas classses derivadas.

from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

p1 = ContaPoupanca(1234, 3245, 0)

p1.depositar(2000)
p1.sacar(10)

print("---------------------------------------")

cc = ContaCorrente(1234, 2453, 0)
cc.sacar(101)