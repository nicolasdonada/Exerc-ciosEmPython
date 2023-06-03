from Utilidades import Validações
from Utilidades import Dados


if not Dados.ArquivoExiste(Validações.arquivo):
    Dados.CriarArquivo(Validações.arquivo)

while True:
    Validações.menu()
    Validações.LerOpção("Opção: ")

    if Validações.exec == False:
        break
     