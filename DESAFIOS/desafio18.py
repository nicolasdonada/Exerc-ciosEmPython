import math

an = float(input("Digite o ângulo que você deseja: "))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print(f"O ângulo de {an} tem o SENO de {s:.2f}")
print(f"O ângulo de {an} tem o COSSENO de {c:.2f}")
print(f"O ângulo de {an} tem o TANGENTE de {t:.2f}")