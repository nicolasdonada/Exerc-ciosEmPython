def ficha(nome=0, gols=0):

    if nome == "":
        nome = "<desconhecido>"

    print(f"O jogador {nome} fez {gols} gols no campeonato.")

nome_jogador = input("Digite o nome o jogador: ")
gols_jogador = input("Digite o número de gols: ")

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0


ficha(nome_jogador, gols_jogador)