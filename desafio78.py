lista = []
continuar = 's'
digitados = 0
while True:
    if continuar == 's':
        num = int(input("Digite um valor"))
        lista.append(num)
        digitados += 1
        continuar = str(input("Quer continuar?")).strip().lower()[0]
    else:
        break
lista.sort(reverse=True)
print(f'Foram digitados {digitados} números')
print(f'A ordem decrescente dos valores digitados é {lista}')
if 5 in lista:
    print('o valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
