media = 0
maior = 0
cont = 0
for c in range(1,5):
    print("-"*5 + f"{c}º pessoa"+"-"*5)
    nome = str(input("Nome")).strip()
    idade = int(input("Idade"))
    sexo = str(input("Sexo[m/f]")).strip()
    media = (media + idade)/4
    if c == 1 and sexo in "Mm":
        maior = idade
        senhor = nome
    elif idade > maior and sexo == "Mm":
        maior = idade
        senhor = nome
    if sexo == "f" and idade < 20:
        cont += 1
print(f"A média de idade do grupo é de {media}")
print(f"o homem mais velho tem {maior} anos e se chama {senhor}")
print(f"Ao todo são {cont} mulheres com menos de 20 anos")
