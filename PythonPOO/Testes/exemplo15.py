#A sobrecarga de operadores em Python permite definir o comportamento de operações como adição, subtração, etc., para tipos de objetos personalizados, utilizando métodos mágicos. Isso possibilita a expressão de operações personalizadas em uma sintaxe familiar.

#__add__(self, other): sobrecarrega o operador de adição (+).
#__sub__(self, other): sobrecarrega o operador de subtração (-).
#__mul__(self, other): sobrecarrega o operador de multiplicação (*).
#__div__(self, other): sobrecarrega o operador de divisão (/).
#__eq__(self, other): sobrecarrega o operador de igualdade (==).
#__lt__(self, other): sobrecarrega o operador de menor que (<).
#__gt__(self, other): sobrecarrega o operador de maior que (>).

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Retangulo(novo_x, novo_y)

r1 = Retangulo(10,2)
r2 = Retangulo(3,5)

retangulo = r1 + r2

print(retangulo.x, retangulo.y)