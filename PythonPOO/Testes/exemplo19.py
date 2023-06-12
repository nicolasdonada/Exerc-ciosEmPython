class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Criação de objetos
autor = Autor("João Silva")
livro = Livro("Python para Iniciantes", autor)

# Acesso aos objetos agregados
print(livro.titulo)  # Saída: Python para Iniciantes
print(livro.autor.nome)  # Saída: João Silva