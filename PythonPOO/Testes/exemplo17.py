#Em Python tudo é um objeto: incluindo classes.
#Metaclasses são "Classes" que criam classes.
#Type é uma metaclasse.

A = type("A", (), {"msg": "Olá, Mundo!"})#Como criar uma classe usando type.

a = A()
print(a.msg)