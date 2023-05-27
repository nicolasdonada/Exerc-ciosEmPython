n1 = float(input("Digite sua primeira NOTA:"))
n2 = float(input("Digite sua segunda NOTA:"))
nota = (n1 + n2) / 2

if nota >=6:
    print(f"PARABÉNS VOCÊ PASSOU DE ANO COM {nota} PONTOS")
else:
    print("INFELIZMENTE VOCÊ NÃO PASSOU DE ANO")