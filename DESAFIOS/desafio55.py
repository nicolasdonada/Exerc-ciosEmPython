menor = 0
maior = 0

for pe in range(1, 6):
    peso = float(input(f"Peso da {pe}ª pessoa: "))

    if pe == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior}Kg")
print(f"O menor peso lido foi {menor}Kg")