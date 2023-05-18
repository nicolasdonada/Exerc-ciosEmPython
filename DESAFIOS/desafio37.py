num = int(input("Digite um número inteiro: "))
print("Escolha uma das opções de conversão abaixo:")
print("[1] converter para BINÁRIO")
print("[2] converter para OCTAL")
print("[3] converter para HEXADECIMAL")
print("[x] para sair")
opcao = str(input("Sua opção: "))

if opcao == "1":
    print(f"{num} convertido para BINÁRIO é {bin(num)[2:]}")

elif opcao == "2":
    print(f"{num} convertido para OCTAL é {oct(num)[2:]}")

elif opcao == "3":
    print(f"{num} convertido para HEXADECIMAL é {hex(num)[2:]}")

else:
    print("Obrigado por utilizar meu programa!!! :)")