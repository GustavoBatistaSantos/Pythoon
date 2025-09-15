#ordem de precedencia de operadores aritiméticos
# ()
# **
# * / // %
# + - #
#nome = input ('Qual é o seu nome?')
#print('prazer em conhece-lo {:^20}!'.format(nome))

n1 = int(input('um valor'))
n2 = int(input('outro valor'))
s = n1+n2
m = n1*n2
d= n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, \n o produto é {},\n e a divisão é {:.3f} '.format(s,m,d), end='')
print (' divisão inteira {} e exponenciação {}'.format(di,e))
#:.3f é 3 casas flutuantes
#end='' é para não quebrar a linha
#\n para quebrar a linha no meio do print