sexo = str(input("Digite seu sexo:[M/F] ")).upper().strip()[0]


'''while sexo not in "MmFf": '''
while sexo != "M" and sexo != "F":
    print("Você informou um valor inválido")
    sexo = str(input("Digite seu sexo novamente:[M/F] ")).upper().strip[0]

print(f"Sexo {sexo} foi registrado")
print("Acabou!!!")
