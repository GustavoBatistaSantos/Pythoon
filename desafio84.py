matriz = [[0,0,0],[0,0,0],[0,0,0]]
total3 = maior = somapar = 0
for l in range (0,3):
    for c in range (0,3): 
        matriz [l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
        if matriz [l][c] % 2 == 0:
            somapar += matriz [l][c]
        if c == 2:
            total3 += matriz [l][c]
        if l == 1 and c == 0:
            maior = matriz [l][c]
        elif l == 1 and c !=0 and matriz[l][c]> maior:
            maior = matriz [l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos números da terceira coluna  é igual a {total3}')
print(f'O maior valor da da linha 2 é {maior}')