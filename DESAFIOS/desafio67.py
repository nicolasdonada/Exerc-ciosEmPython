while True:
    print("-" * 20)
    n = int(input("Digite o valor desejado para ver sua tabuada: "))
    print("-" * 20)
    if n <= -1:
        break
    for c in range(1,11):
        so = n * c     
        print(f"{c} X {n} = {so}")

print("Obrigado por utilizar meu programa!!!")