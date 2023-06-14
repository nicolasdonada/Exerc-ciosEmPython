from Classes.conta1 import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print("O valor precisa ser númerico!")
            return
        
        if self.saldo < valor:
            print("Valor desejado para saque maior que o saldo!!")
            return
        
        self.saldo -= valor
        self.detalhe()