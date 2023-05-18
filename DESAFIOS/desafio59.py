num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
sair = False

while not sair:
    print('''=-=-=-=-=-=-=-=-=-=-=-=
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
    opcao = int(input("Qual a sua opção? "))

    if opcao == 1:
        print(f"A soma entre {num1} + {num2} = {num1 + num2}")
    
    elif opcao == 2:
        print(f"A multiplição entre {num1} X {num2} = {num1 * num2}")
    
    elif opcao == 3:
        if num1 > num2:
            print(f"O maior valor entre {num1} e {num2} é {num1}")
        else:
            print(f"O maior valor entre {num1} e {num2} é {num2}")
    
    elif opcao == 4:
        print("Informe novamente os valores:")
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    
    elif opcao == 5:
        sair = True
    
    else:
        print("Opçãp inválida. Tente novamente")

print("Obrigado por utilizar meu sistema!! :)")