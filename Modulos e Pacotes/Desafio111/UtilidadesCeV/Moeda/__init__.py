def dobro(n1=0, format=False):
    res = n1 * 2
    return f"R${res:.2f}".replace(".", ",") if format is False else f"R${res}"

def aumentar(n1=0, taxa=0, format=False):
    n = (n1 * taxa) / 100
    res = n1 + n
    return f"R${res:.2f}".replace(".", ",") if format is False else f"R${res}"

def metade(n1=0, format=False):
    res = n1 / 2
    return f"R${res:.2f}".replace(".", ",") if format is False else f"R${res}"

def diminuir(n1=0, taxa=0, format=False):
    por = (n1 * taxa) / 100
    res = n1 - por
    return f"R${res:.2f}".replace(".", ",") if format is False else f"R${res}"

def moeda(res = 0, moeda = "R$", format=False):
    return f"{moeda}{res:.2f}".replace(".", ",") if format is False else f"R${res}"

def resumo(n1, aumento=12, diminui=6):
    print("-" * 20)
    print("  RESUMO DO VALOR")
    print("-" * 20)
    print(f"Preço analisado: \t{moeda(n1)}")
    print(f"Dobro do preço: \t{dobro(n1)}")
    print(f"Metado do preço: \t{metade(n1)}")
    print(f"{aumento}% de aumento: \t{aumentar(n1, aumento)}")
    print(f"{diminui}% de redução: \t{diminuir(n1, diminui)}")
    print("-" * 20)
    