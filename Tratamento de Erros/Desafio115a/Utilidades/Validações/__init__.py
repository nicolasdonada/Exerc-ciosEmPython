from Utilidades import Dados
from time import sleep

arquivo = "arquivo.txt"

def menu(): #Função para mostrar as opções do programa
    print("-" * 30)
    print("        MENU PRINCIPAL")
    print("-" * 30)
    print("\033[0;33m1 -\033[m\033[0;34m Ver pessoas cadastras\033[m")
    print("\033[0;33m2 -\033[m\033[0;34m Cadastrar nova pessoa\033[m")
    print("\033[0;33m3 -\033[m\033[0;34m Sair\033[m")

def LerOpção(num): #Função para validar e ler a opção 
    global exec
    exec = True
    sleep(1)

    while True:
        try:
            opcao = int(input(num))

            while True:

                if opcao > 3 or opcao <= 0:
                    print("\033[0;31mERRO! Você digitou algo inválido.\033[m")
                    opcao = int(input(num))
                else:
                    opcao = int(opcao)
                    break

        except(TypeError, ValueError, KeyboardInterrupt):
            print("\033[0;31mERRO! Você digitou algo inválido.\033[m")
            continue

        else:
            break
    
    if opcao == 1:
        Dados.Ver(arquivo)

    if opcao == 2:
        LerNomeIdade(arquivo)

    if opcao == 3:
        print("\033[0;31mDesligando o programa....\033[m")
        exec = False

def LerNomeIdade(ar): #Função para validar e ler o nome e a idade
    sleep(1)
    
    print("\033[0;33m-" * 40)
    print("      CADASTRANDO UMA NOVA PESSOA")
    print("-" * 40,'\033[m')

    while True:
        nome = str(input("Nome: ")).strip()

        if nome.isdecimal():
            print("\033[0;31mERRO! Você digitou algo inválido.\033[m")

        if nome == "":
            print("\033[0;31mERRO! Você digitou algo inválido.\033[m")

        else:
            break
    
    while True:
        try:
            idade = int(input("Idade: "))

        except(TypeError, ValueError, KeyboardInterrupt):
            print("\033[0;31mERRO! Você digitou algo inválido.\033[m")
            continue
        
        else:
            break
        
    Dados.Cadastro(ar, nome, idade)
    print("\033[0;32m    CADASTRADO COM SUCESSO!!!\033[m")