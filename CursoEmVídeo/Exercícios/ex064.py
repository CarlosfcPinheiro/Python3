#Tratamento de Valores
from time import sleep

count = 0
sum = 0
print('Esse Programa irá receber números inteiros em exceção de 999, que é a condição de parada. Sendo assim:')
number = int(input('Digite um número: '))
upper = 0
lower = 0
while number != 999:
    upper = number
    lower = number
    count += 1
    sum += number
    number = int(input('Digite um número: '))
    if number < upper and number != 999:
        upper = number
    elif number > lower and number != 999:
        lower = number
print('\nAnalisando Dados...')
sleep(3)
print('QUANTIDADE DE NÚMEROS DIGITADOS: {0}'.format(count))
print('SOMA DOS NÚMEROS DIGITADOS (exceção de 999): {0}'.format(sum))
print('O MAIOR NÚMERO: {0}'.format(upper))
print('O MENOR NÚMERO: {0}'.format(lower))
