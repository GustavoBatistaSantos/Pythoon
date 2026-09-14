matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):# porque são 3 elementos nas linhas
    for c in range (0,3): # porque são 3 elementos dentro de cada linha
        matriz [l][c] = int(input(f'digite um valor para [{l}, {c}]: '))#o l,c serve para adicionar o valor aos 2 laços
        #o elemento do laço de baixo e executado inteiro para ser executado o próxima laço de cima
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print() #mostra o print de cima após sair do laço de baixo