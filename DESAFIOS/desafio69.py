con = 0
c = 0
c1 = 0

while True:
    print("=-" * 20) 
    print("         CADASTRO DE CLIENTE") 
    print("=-" * 20) 
    idade = int(input("Digite sua idade: "))
    idade2 = idade

    if idade2 > 18:
        con += 1

    sexo = str(input("Digite seu sexo[M/F]: ")).upper().strip()
    while sexo != "M" and sexo != "F":
        sexo = str(input("Digite seu sexo[M/F]: ")).upper().strip()
    sexo1 = sexo
    if sexo == "M":
        c += 1
    if sexo == "F" and idade2 < 20:
        c1 += 1
        
    print("=-" * 20) 
    fim = str(input("Você deseja continuar[S/N]?")).upper().strip()
    while fim != "S" and fim != "N":
        print("=-" * 20) 
        fim = str(input("Você deseja continuar[S/N]?")).upper().strip() 

    if fim == "N":
        break
print("=-" * 20)    
print(f"Total de {con} pessoas que tem mais de 18 anos.")
print(f"Total de {c} homens cadastrados.")
print(f"Total de {c1} mulheres que tem menos de 20 anos.")
print("=-" * 20) 