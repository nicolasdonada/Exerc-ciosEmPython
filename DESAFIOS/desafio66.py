con = 0
num = 0

while True:
    n = int(input("Digite um valor[999 para sair]: "))

    if n == 999:
        break
    con += 1
    num += n

print(f"Foi digitado um total de {con} números\nA soma entre os números foi {num}")