'''Nu = int(input("Quantos termos deseja mostrar? "))
c = 1
u1 = 1
u2 = 1
t = 0

while c <= Nu: 
    print(u1, end=" -> ")
    temp = u1
    u1 = u2
    u2 = temp + u1
    c += 1

print("FIM")'''

print("=-" * 15)
print("Sequência de Fibonacci")
print("=-" * 15)

nu = int(input("Quantos termos deseja mostrar? "))
print("=-" * 15)

u1 = 0
u2 = 1

for c in range(0,nu):
    print(u1, end=" -> ")
    u3 = u1
    u1 = u2
    u2 = u3 + u1

print("FIM")