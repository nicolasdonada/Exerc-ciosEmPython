from Classes.cliente import Cliente
from Classes.contacorrente import ContaCorrente
from Classes.contapoupanca1 import ContaPoupanca
from Classes.banco1 import Banco


banco = Banco()


cliente_1 = Cliente("Nicolas", 20)
conta_1 = ContaCorrente(cliente_1, 1234, 21312, 100)

print(f"Conta do {cliente_1.nome}")
conta_1.depositar(100)

print(f"Conta do {cliente_1.nome}")
conta_1.sacar(200)



cliente_2 = Cliente("João", 19)
conta_2 = ContaPoupanca(cliente_2, 1111, 12367, 100)
banco.inserir_cliente(cliente_2)
banco.inserir_conta(conta_2)


print(f"Conta do {cliente_2.nome}")


if banco.autenticar(conta_2) == True:
    conta_2.depositar(10000)
    conta_2.sacar(100)
else:
    print("Conta inválida!")