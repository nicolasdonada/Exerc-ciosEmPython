idade = int(input("Digite a sua IDADE: "))
altura = float(input("Digite a sua ALTURA:(M) "))
peso = float(input("Digite o seu PESO:(Kg) "))

imc = peso / (altura * altura) 
print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print("Você está abaixo do seu peso ideal")

elif imc >= 18.5 and imc <= 25:
    print("Òtimo você está no seu peso ideal")

elif imc > 25 and imc <= 30:
    print("Péssima notícia você está acima do seu peso ideal")

elif imc > 30 and imc <= 40:
    print("Urgente você está em obesidade CUIDADO!!!!")

else:
    print("PERIGO!! você está em OBESIDADE MÓRBIDA")