def maior(* num):
    maior = 0

    print("Analisando os valores passados...")

    for n in num:
        if n == 1:
            maior = n

        else:
            if n > maior:
                maior = n
        print(n, end=" ")
    print(f"Foram informados ao todo {len(num)} valores.")
    print(f"O maior valor informado foi {maior}.")
    print("-=" * 10)


maior(3,6,2,7)
maior(9,32,5,65)
maior(999,4,54,3,623)