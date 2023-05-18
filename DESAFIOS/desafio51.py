print("=-" * 10)
print("10 TERMOS EM PA")
print("=-" * 10)

p = int(input("Primeiro termo: "))
r = int(input("Razão: "))
m = p + (10 - 1) * r

for c in range(p, m + r, r):
    print(c, end=" -> ")
print("FIM")