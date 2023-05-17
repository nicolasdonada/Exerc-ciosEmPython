def nome_usuario(nome):
    mensagem = "Olá " + nome + ", Bem Vindo!"
    return mensagem


while n == True:
    n = input("Digite seu nome: ")
    r = nome_usuario(n)
    print(r)
