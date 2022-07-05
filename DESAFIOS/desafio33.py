v1 = int(input("Primeiro valor:"))
v2 = int(input("Segundo valor:"))
v3 = int(input("Terceiro valor:"))

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print(f"O menor número digitado é {menor}")

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f"O maior número digitado é {maior}")