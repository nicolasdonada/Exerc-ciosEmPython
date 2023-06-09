#Criando exceções

class TaErrado(Exception):
    pass

def dividir(a, b):
    if b == 0:
        raise TaErrado("Não é permitido dividir por 0")
    
    return a / b

try: 
    resultado = dividir(2, 2)
    print(f"Resultado: {resultado}")

except TaErrado as error:
    print(f"Ocorreu um erro: {error}")