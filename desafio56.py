n1 = int(input("Qual é o primeiro número?"))
n2 = int(input("Qual é o segundo número?"))
opcao = 0 
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual é a sua opcão? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a soma')
        opcao = 5
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação de {n1} e {n2} é igual a {multiplicacao}')
        opcao = 5
    elif opcao == 3:
        