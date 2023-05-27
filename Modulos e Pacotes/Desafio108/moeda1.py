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