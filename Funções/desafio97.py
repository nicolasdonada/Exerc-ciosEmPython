def escreva(pala):
    tam = len(pala) + 4
    print("-" * tam)
    print(f"  {pala}")
    print("-" * tam)

    
while True:
    palavra = str(input("Palavra: "))
    escreva(palavra)

    inte = str(input("Deseja continuar[S/N]:")).upper()
    if inte == "N":
        break