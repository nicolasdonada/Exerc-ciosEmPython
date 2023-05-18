import random
con = 0
print("-=" * 20)
print("Bem Vindo ao Jogo do PAR E IMPAR")
print("-=" * 20)

while True:

    pc = random.randint(1, 10)
    usuario = int(input("Digite um valor: "))
    pi = str(input("Ímpar ou Par?[P/I] ")).upper().strip()
    while pi != "P" and pi != "I":
        pi = str(input("Ímpar ou Par?[P/I] ")).upper().strip()

    soma = pc + usuario
    print("-=" * 20)
    print(f"VOCÊ jogou {usuario} e o COMPUTADOR jogou {pc}. Somando um total de {soma}")
    print("-=" * 20)

    if soma % 2 == 0 and pi == "P":
        print("Parabéns você VENCEU!!")
        print("Vamos jogar novamente....")
        print("-=" * 20)
        con += 1

    if soma % 2 != 0 and pi == "I":
        print("Parabéns você VENCEU!!")
        print("Vamos jogar novamente...")
        print("-=" * 20)
        con += 1
    
    if soma % 2 == 0 and pi != "P":
        print("Infelizmente você PERDEU")
        print(f"Você VENCEU {con} vezes consecuitivas.")
        print("-=" * 20)
        break
    if soma % 2 != 0 and pi != "I":
        print("Infelizmente você PERDEU")
        print(f"Você VENCEU {con} vezes consecutivas.")
        print("-=" * 20)
        break