from time import sleep



def Ver(nome): #Função para mostrar a lista de pessoas cadastradas
    sleep(1)

    print("\033[0;32m-" * 30)
    print("     LISTA DE CADASTROS")
    print("-" * 30, '\033[m')

    try:
        a = open(nome, "rt")
    except:
        print("ERRO ao ler o arquivo")
    else:
        for linha1 in a:
            linha = linha1.split(";")
            linha[1] = linha[1].replace("\n", "") 
            print(f"Nome: {linha[0]} - Idade: {linha[1]}")
    finally:
        a.close()

def Cadastro(ar, nome, idade): #Função para cadastrar a pessoa
    try:
        a = open(ar, "at")
    except:
        print("ERRO: não foi possivel abrir o arquivo.")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados")
        else:
            a.close()

def ArquivoExiste(nome):
    try:
        a = open(nome)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("ERRO na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")
