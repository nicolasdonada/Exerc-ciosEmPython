from datetime import date

con = 0
con2 = 0
ano = date.today().year

for c in range(1,8):
    num = int(input(f"Em que ano a {c} pessoa nasceu? "))
    
    if ano - num >= 18:
        con += 1
        
    elif ano - num < 18:
        con2 += 1

print(f"Total de pessoas maiores de idade: {con}")
print(f"Total de pessoas menores de idade: {con2}")
