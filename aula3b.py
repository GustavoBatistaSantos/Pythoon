n = float(input ('digite um valor'))
#4
print(n)
# vai mostrar 4.0

n = input('digite algo')
print('o tipo primitivo desse valor é',type(n))
print('É um número ?', n.isnumeric())#para perguntar se é um número
print('É alfabetico ?', n.isalpha())#para perguntar se é letra
print('É alphanumérico?', n.isalnum())#para perguntar se é letra ou número
print('Está em maiusculas?', n.isupper())#para perguntar se é so com letras maiusculas
print(n.isascii())
print(n.isdecimal())#para verificar se é decimal 
print(n.isdigit())#para verificar se é um digito
print('esta em minusculas ?', n.islower())#para verificar se é apenas letras minusculas 
print(n.isidentifier())#para verificar se é um identificador válido
print(n.isprintable())
print('So tem espaços?',n.isspace())#para verificar se tem espaço em branco
print('Está capitalizada', n.istitle())#esta capitalizada primeira maiuscula e outras minusculas