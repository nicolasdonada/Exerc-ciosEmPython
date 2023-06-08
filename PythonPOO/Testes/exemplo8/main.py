from classes import CarrinhoDeCompra, Produto

carrinho = CarrinhoDeCompra()

p1 = Produto("Calça", 80)
p2 = Produto("Chinelo", 30)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

carrinho.listar_produtos()
print(carrinho.somar_produto())