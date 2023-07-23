conta_banco = 0
limite_diario = 0
limite_saque = 500

while True:

    print("[1] Depósito\n[2] Saque\n[3] Saldo")
    
    opcao_banco = int(input("Digite sua opção: "))

    while opcao_banco != 1 and opcao_banco != 2 and opcao_banco != 3:
        print("[1] Depósito\n[2] Saque\n[3] Saldo")
        opcao_banco = int(input("Digite sua opção: "))


    if opcao_banco == 1:

        try:
            valor_deposito = float(input("Digite o valor desejado para depósitar: R$"))
        except (TypeError, ValueError) as erro:
            print("Digite um valor válido!!")
            valor_deposito = float(input("Digite o valor desejado para depósitar: "))
        
        print("Depósito realizado com sucesso!")
        conta_banco += valor_deposito

    if opcao_banco == 2:
        print(f"Quantidade de saques disponiveis {limite_diario}/3")


        try:
            if limite_diario >= 3:
                print("Número total de saques já realizados!!")
                continue

            valor_saque = float(input("Valor desejado de saque: R$"))
            if valor_saque > limite_saque:
                print("Valor permitido de saque até R$500.00")
                valor_saque = float(input("Valor desejado de saque: R$"))


        except( ValueError, TypeError) as erro:
            if limite_diario >= 3:
                print("Número total de saques já realizados!!")
                continue

            print("Digite um valor válido!!")
            valor_saque = float(input("Valor desejado de saque: R$"))

            if valor_saque > limite_saque:
                print("Valor permitido de saque até R$500.00")
                valor_saque = float(input("Valor desejado de saque: R$"))

        conta_banco -= valor_saque
        limite_diario += 1

    if opcao_banco == 3:
        print(f"Saldo da Conta: R${conta_banco:.2f}")

