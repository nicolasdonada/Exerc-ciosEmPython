from re import U


nu = int(input("Digite um número:"))

u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10

print(f"Analisando o número {nu}......")
print(f"Unidades: {u}")
print(f"Dezenas: {d}")
print(f"centenas: {c}")
print(f"Milhares: {m}")