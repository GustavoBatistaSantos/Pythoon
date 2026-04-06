frase='  Curso de Analise e desenvolvimento de Sistemas  '
print(frase[3])#fatiamento da 4 letra
print(frase[3:15])#fatiamento da 4 letra até o 14
print(frase[:15])#fatiamento da 1 letra até o 14
print(frase[15:])#fatiamento da 14 letra até a última
print(frase[1:15:2])#fatiamento da 1 letra até o 14 pulando de 2 em 2
print(frase[1::2])#fatiamento da 1 letra até a ultima pulando de 2 em 2
print(frase.upper().count('o'))#deixa tudo maiuscula em conta quantas vezes tem a letra o
print(len(frase.strip()))#conta os caracteres e tira os espaços 
print(frase.replace('Sistemas','Python'))#troca a palavra sistemas por python
print('Curso' in frase)#verifica se a palavra curso esta na váriavel frase 
print(frase.lower().find('curso'))#transforma as palavras em minusculos e mostra a posição que começa a palavra curso 
print(frase.split())#mostra a frase separada em uma lista 
dividido = frase.split()
print(dividido[0])#mostra a posição 0
print(dividido[2][3])#mostra a posição 0 e a letra 2 da posição 2
