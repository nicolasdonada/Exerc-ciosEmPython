frase = str(input("Digite seu nome completo:")).strip()

ma = frase.upper()
mi = frase.lower()
qu = frase.split()

print("Processando seu nome.....")
print(f"Seu nome em letras maiúsculas é {ma}")
print(f"Seu nome em letras minúsculas é {mi}")
print(f"Seu primeiro nome tem {len(qu[0])} letras")
print(f"Seu nome completo tem {len(frase) - frase.count(' ')} letras")