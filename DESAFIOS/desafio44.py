print("========== LOJAS AMERICANAS ==========")
valor = float(input("Valor das compras? R$"))
print("[1] á vista dinheiro/cheque")
print("[2] á vista no cartão")
print("[3] em até 2x no cartão")
print("[4] 3x ou mais no cartão")

opcao = int(input("Qual a sua opção? "))

if opcao == 1:
    novo = valor * 10/100
 
    print(f"O valor de R${valor} pagando á vista no dinheiro/cheque terá um desconto de 10%, então ficara R${valor - novo}")
elif opcao == 2:
    novo2 = valor * 5/100
   
    print(f"O valor de R${valor} pagando á vista no cartão terá um desconto de 5%, então ficara R${valor - novo2}")
elif opcao == 3:
    parcela = int(input("Digite em quantas vezes: "))

    if parcela <= 2:
        novo3 = valor / parcela
        print(f"Parcelando em {parcela} sairá por R${novo3} por mês")
    else:
        print("Para parcelar acima de 2x selecione a opção número 4")

elif opcao == 4:
    parcela = int(input("Digite em quantas vezes: "))

    if parcela >= 3:
        novo4 = valor / parcela
        juros = (novo4 * 20/100) + novo4
        print(f"O valor de R${valor} parcelando em 3x ou mais no cartão terá 20% de juros, então saira por R${juros}")
    else:
        print("Para parcelar abaixo de 3x selecione a opção 3")
else:
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!!!")
