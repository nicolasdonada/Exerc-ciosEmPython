'''con = 1

while True:
    print(con," -> ", end="")
    con += 1

    if con == 11:
        break
print("FIM")'''
num = 0

while True:
    n = int(input("Digite um número:[999 para sair] "))

    if n == 999:
        break
    num += n
print(f"a soma de todos os números digitados foi {num}")
print("Obrigado por utilizar meu programa!!!")