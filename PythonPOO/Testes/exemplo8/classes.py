class CarrinhoDeCompra:

    def __init__(self):
        self.carrinho = []

    def inserir_produto(self, produto):
        self.carrinho.append(produto)

    def listar_produtos(self):
        for produto in self.carrinho:
            print(produto.produto, produto.valor)

    def somar_produto(self):
        total = 0
        for produto in self.carrinho:
            total += produto.valor
        
        return total

class Produto:

    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor