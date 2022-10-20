import math

print("=-" * 10)
print("Bora fazer uma PA?")
print("=-" * 10)

p = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
c = 1
t = p
to = 0
mais = 10

while mais != 0:
    to += mais
    while c <= to:
        t += r
        c += 1
        print(t, end=" -> ")
    print("PAUSA")
    mais = int(input("Quantos termos você deseja mostrar a mais? "))

print(f"Progressão finalizada com {c - 1} termos mostrados.")