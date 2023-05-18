f = str(input("Escreva uma frase:")).strip().upper()

n = f.count("A")
p = f.find("A") + 1
u = f.rfind("A") + 1
print(f"A letra A aparece {n} vezes na frase")
print(f"A primeira letra A aparece na posição {p}")
print(f"A última letra A apareceu na posição {u}")