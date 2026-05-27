num = int(input("Digite um número "))
tot = 0
for c in range(1,num +1):
    if num % c ==0:
        tot += 1
print(f"O número {num} é  divisivel {tot} vezes")
if tot == 2:
    print("E por isso ele é um número primo")
else:
    print("E por isso ele não é um número primo")