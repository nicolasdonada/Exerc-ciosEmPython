dias = int(input("Quantos dias o carro foi alugado? "))
kms = float(input("Quantos Km você rodou? "))

a = dias * 60
b = kms * 0.15

print(f"O total a pagar é R${b + a:.2f}")