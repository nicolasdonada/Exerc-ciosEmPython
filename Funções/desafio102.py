def fat(nums, mos=False):

    fato = 1
    for num in range(nums, 0, -1):
        fato *= num
        if mos:
            print(num, end=" X ")

        if num == 1:
            print(end="= ")
    return fato

numeros = int(input("Digite um número: "))
print(f"O fatorial de {numeros} é: ")
print(fat(numeros, True))

