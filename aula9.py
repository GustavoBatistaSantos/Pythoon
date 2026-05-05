nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("Que nome bonito!")
elif nome == "Paulo" or nome == "Maria" or nome == "Pedro":
    print("Seu nome é bem popular no Brasil")
elif nome in " Ana Claudia Jéssica Juliana":
    print("Que belo nome feminino")
else:
    print("Seu nome é bem normal")
print("Tenha um bom dia {}".format(nome))