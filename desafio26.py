velocidade = float(input("Qual é a velocidade atual do carro? "))
multa = (velocidade-80)*7
if velocidade<=80:
    print("Tenha um bom dia! Dirija com segurança")
else:
    print("Multado! Você excedeu o limite permitido que é de 80Km/h. Você deve pagar uma multa de R${:.2f}!".format(multa))