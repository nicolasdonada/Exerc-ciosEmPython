from time import sleep

def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(1)
    cont = i

    if p == 0:
        p = 1

    if i < f:
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)  
            cont += p  
        print("FIM!")

    else:
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")

    
    

contador(0, 10, 1)
contador(10, 0, 2)

print("Sua vez!")
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))

contador(inicio, fim, abs(passo))