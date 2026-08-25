lista  = []
par = []
impar = []
continuar = 's'
while True:
    if continuar == 's':
        num = int(input("Digite um valor"))
        lista.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
        continuar = str(input('quer continuar?')).lower().strip()[0]
    else:
        break
print(f'Os valores digitados foram{lista}, sendo os números {par} pares e os números{impar} imapares' )


    
    