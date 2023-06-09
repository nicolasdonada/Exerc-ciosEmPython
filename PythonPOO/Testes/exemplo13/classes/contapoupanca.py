from classes.conta import Conta

class ContaPoupanca(Conta):

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor precisa ser númerico")

        if self.saldo < valor:
            print("Saldo menor que valor desejado para sacar")
            return
        
        self.saldo -= valor
        self.detalhe()  
    