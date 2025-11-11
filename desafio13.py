dias = int(input('Quantos dias alugados?'))
Km = float(input('Quantos Km rodados?'))
diaria = dias*60
percurso = Km * 0.15
custo = diaria + percurso

print('o total a pagar é de R${:.2f}'.format(custo))