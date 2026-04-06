numero = int(input('informe um número'))
u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10
print('Analisando {}'.format(numero))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centana {}'.format(c))
print('milhar {}'.format(m))