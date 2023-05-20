def Ler_Int(a):
    num = input(a)

    if num.isdecimal():
        num = int(num)
        print(f"Você acabou de digitar o número {num}")
    else:
        print("\033[0;34mValor errado\033[m")
        Ler_Int("Digite um número: ")



Ler_Int("Digite um número: ")
