#Desafio simples sobre getter e setter

class ContaBancaria:

    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("ERRO! Valor maior que o saldo.")

    
p1 = ContaBancaria("Pedro")

print(f"Bem Vindo! Senhor {p1.nome}.")
print(f"Saldo Inicial: {p1.saldo}")
p1.depositar(100)
print(f"Saldo Inicial: {p1.saldo}")
p1.sacar(101)
print(f"Saldo Inicial: {p1.saldo}")



