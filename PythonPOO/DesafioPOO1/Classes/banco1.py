class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []
        '''self.cliente = cliente
        self.conta = conta'''
    '''def checar(self):
        if self.cliente.nome in self.conta.cliente.nome:
            return True
        else:
            return False'''
    
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, conta):
        if conta not in self.contas:
            return False
        
        if conta.cliente not in self.clientes:
            return False
        
        if conta.agencia not in self.agencias:
            return False
        
        return True