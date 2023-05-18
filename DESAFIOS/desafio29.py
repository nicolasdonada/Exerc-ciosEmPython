velo = int(input("Digite a sua velocidade:"))
multa = (velo - 80) * 7

if velo <=80:
    print(f"Muito bem sua velocidade é de {velo}Kmph, você não irá tomar multa.")
else:
    print(f"Infelizmente sua velocidade foi de {velo}Kmph, você terá que pagar uma multa de R${multa}")