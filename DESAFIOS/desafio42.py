l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Formam um triângulo")
    if l1 == l2 == l3:
        print("Os valores digitados FORMAM um TRÂNGULO EQUILÁTERO")

    elif l1 != l2 != l3 != l1:
        print("Os valores digitados FORMAM um TRÂNGULO ESCALENO")

    else:
        print("Os valores digitados FORMAM um TRÂNGULO ISÓSCELES")
    
else:
    print("Os valores digitados NÃO PODEM FORMAR UM TRIÂNGULO")