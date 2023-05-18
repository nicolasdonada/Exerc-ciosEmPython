num = int(input("Digite um número: "))
con = 0

for c in range(1, num + 1):
    if num % c == 0:
        print("\033[0;33m", end=" ")
        con += 1
    else:
        print("\033[31m", end=" ")

    print(c, end=" ")
print(f"\n\033[mO número {num} foi divisivel {con} vezes")

if con == 2:
    print("Por isso ele é PRIMO")     
    
else:
    print(f"O valor {num} digitado não é um número PRIMO")