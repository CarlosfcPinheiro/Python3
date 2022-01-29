#Cálculo Fatorial
from time import sleep

num = int(input('Digite um número inteiro para calcular seu fatorial: '))
print('Calculando...')
sleep(3)
decress = num
factorial = 1
print('\033[0;31mResultado {0}!:\033[0;33m'.format(num), end=' ')
while decress > 0:
    print('{0}'.format(decress), end=' ')
    if decress > 1:
        print('x', end=' ')
    else:
        print('=',end=' ')
    factorial *= decress
    decress -= 1
print(factorial)



