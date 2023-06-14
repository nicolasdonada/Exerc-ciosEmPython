from abc import ABC, abstractmethod
from Classes.cliente import Cliente

class Conta(ABC, Cliente):
    def __init__(self, cliente, agencia, conta, saldo):
        self._cliente = cliente
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def cliente(self):
        return self._cliente
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            print("Valor precisa ser númerico.")
            return
        
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            print("Valor precisa ser númerico.")
            return
        
        self.saldo += valor
        self.detalhe()

    @abstractmethod
    def sacar(self):
        pass

    def detalhe(self):
        print(f"Agência: {self.agencia} Conta: {self.conta} Saldo: {self.saldo}")
        print()