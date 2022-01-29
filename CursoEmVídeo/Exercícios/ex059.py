#Tela de Menu para dois números
from time import sleep

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
option = 4
while option != 5:
    option = int(input('''Agora, informe oque você deseja fazer com esses números de acordo com as opções a seguir:
     {0}=
     [ 1 ] SOMAR
     [ 2 ] MULTIPLICAR
     [ 3 ] QUAL É O MAIOR
     [ 4 ] ADICIONAR NOVOS 2 NÚMEROS
     [ 5 ] ---> SAIR DO PROGRAMA <---
     {0}=
     Informe aqui a sua opção: '''.format('=-'*20)))
    if option == 1:
        sum = num1 + num2
        print('A soma entre os números {0} e {1} resulta em: {2}'.format(num1, num2, sum))
        sleep(3)
    elif option == 2:
        mult = num1 * num2
        print('A multiplicação entre os números {0} e {1} resulta em: {2}'.format(num1, num2, mult))
        sleep(3)
    elif option == 3:
        if num1 > num2:
            print('O maior número é: {0}'.format(num1))
            sleep(3)
        elif num2 > num1:
            print('O maior número é: {0}'.format(num2))
            sleep(3)
        else:
            print('Os números informados são iguais.')
            sleep(3)
    elif option == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    elif option == 5:
        print('Encerrando processo...')
        sleep(3)
        print('''        Obrigado por usar!
        Volte sempre :)''')
    else:
        print('Desculpe essa opção é inválida')
        sleep(3)



