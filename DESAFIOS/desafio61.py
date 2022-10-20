print("=-" * 10)
print("Bora fazer uma PA?")
print("=-" * 10)

p = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
c = 1
t = p

while c <= 10:
    print(t, end=" -> ")
    t += r
    c += 1

print("FIM")
