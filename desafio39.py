print("-=-" * 10)
print("Analisador de triângulos")
print("-=-" * 10)
a = float(input("Primeiro segmento "))
b = float(input("Segundo segmento "))
c = float(input("Terceiro segmento "))
if a<b+c and b<a+c and c<a+b and a== b == c:
    print("Os segmentos acima podem formar um triangulo Equilatero")
elif a<b+c and b<a+c and c<a+b and a== b or a== c or b==c:
    print("Os segmentos acima podem formar um triangulo Isósceles")
elif a<b+c and b<a+c and c<a+b and a!= b and a!= c and b!=c:
    print("Os segmentos acima podem formar um triangulo Escaleno")
else:
    print("os segmentos acima não podem formar um triangulo")