s = 0
n = 0
t = 0

while n != 999:
    n = int(input("Digite um número [999 para sair]: "))
    if n < 999:
        s += n
        t += 1
    else:
        n += 0

print(f"Você digitou {t} números e a soma entre eles é {s}.")