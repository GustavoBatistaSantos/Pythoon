real = float (input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/5.36
print ('Com R${:.2F} você pode comprar US${:.2f}'.format(real,dolar))