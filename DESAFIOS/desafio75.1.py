nums = (int(input("Digite um valor:")), int(input("Digite um valor:")), int(input("Digite um valor:")), int(input("Digite um valor:")))


print(f"O valor 9 apareceu {nums.count(9)} vezes")

if 3 in nums:
    print(f"O número 3 apareceu na posição {nums.index(3)+1}ª")
else:
    print("O número 3 não foi encontrado.")
print(f"os números pares são: ", end="")

for n in nums:
    if n % 2 == 0:
        print(n, end=" ")