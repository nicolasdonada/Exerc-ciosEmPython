print("~" * 50)
print("Se você viajar por até 200km, você terá que pagar R$0.50 por KM\nSe a sua viagem passar de 200KM, você terá que pagar R$0.45 por KM")
print("~" * 50)
distancia = int(input("Digite a distância de sua viagem:"))
preco = distancia * 0.50
preco2 = distancia * 0.45

if distancia <=200:
    print(f"Se você viajar por {distancia}KM, você tera que pagar uma passagem de R${preco:.2f}")
else:
    print(f"Se você viajar por {distancia}KM, você tera que pagar uma passagem de R${preco2:.2f}")