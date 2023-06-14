from Classes.conta1 import Conta

class ContaCorrente(Conta):

    def __init__(self, cliente, agencia, conta, saldo, limite=100):
        super().__init__(cliente, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite
    

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            print("O valor precisa ser númerico")
            return
        
        if (self.saldo + self.limite) < valor:
            print("Valor desejado para saque maior que o saldo!!")
            return

        self.saldo -= valor
        self.detalhe()