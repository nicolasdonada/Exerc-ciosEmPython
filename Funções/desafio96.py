def area():
    print("---- CALCULADORA DE ÁREA ----")

    lar = float(input("Digite a largura do terreno(M): "))
    com = float(input("Digite o comprimento do terreno(M): "))

    ar = lar * com

    print(f"Um terreno de {lar}x{com} tem a área de {ar}m².")

area()