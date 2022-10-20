print("~=" * 20)
print("Analisador de Triângulos")
print("~=" * 20)
n1 = float(input("Digite o primeiro valor:"))
n2 = float(input("Digite o segundo valor:"))
n3 = float(input("Digite o terceiro valor:"))

lista = [n1, n2, n3]

if n1 + n2 + n3 - max(lista) > max(lista):
    print("Os segmentos acima PODEM formar um triângulo.")
else:
    print("OS segmentos acima NÃO PODEM formar um triângulo.")