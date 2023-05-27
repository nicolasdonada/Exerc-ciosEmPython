def LerDinheiro(numero):
    valido = False

    while not valido:
        entrada = str(input(numero)).strip()

        if entrada.isalpha():
            print(f"ERRO! o valor '{entrada}' é inválido.")
            LerDinheiro("Digite um valor: R$")

        if entrada.isspace():
            print(f"ERRO! o valor '{entrada}' é inválido.")
            LerDinheiro("Digite um valor: R$")

        if entrada == "":
            print(f"ERRO! o valor '{entrada}' é inválido.")
            LerDinheiro("Digite um valor: R$")

        else:
            valido = True
            return float(entrada.replace(",", "."))
