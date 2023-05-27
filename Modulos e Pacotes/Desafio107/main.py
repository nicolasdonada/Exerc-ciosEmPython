import moeda

valor = float(input("Digite um valor: R$"))

print(f"O dobro de R${valor:.2f} é R${moeda.dobro(valor)}")
print(f"Aumentando 10% de R${valor} é R${moeda.aumentar(valor)}")
print(f"Diminuindo 10% de R${valor} è R${moeda.diminuir(valor)}")
print(f"A metade de R${valor} é R${moeda.metade(valor)}")