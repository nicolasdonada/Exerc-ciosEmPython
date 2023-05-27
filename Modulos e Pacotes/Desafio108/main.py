import moeda1

valor = float(input("Digite um valor: R$"))

print(f"O dobro de {moeda1.moeda(valor)} é {moeda1.dobro(valor, True)}")
print(f"Aumentando 10% de {moeda1.moeda(valor)} é {moeda1.aumentar(valor, 10, True)}")
print(f"Diminuindo 10% de {moeda1.moeda(valor)} è {moeda1.diminuir(valor, 10, True)}")
print(f"A metade de {moeda1.moeda(valor)} é {moeda1.metade(valor)}")