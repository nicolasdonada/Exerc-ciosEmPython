nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    per = int(input("Digite um número de 0 a 20: "))

    if per >= 0 and per <= 20:
        print(f"O número digitado foi {nums[per]}")
        break
    else:
        print("Número inválido! ")
