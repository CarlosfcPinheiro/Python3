#Square root

import math

num = int(input('Digite um número menor que 500: '))
result = math.sqrt(num)

if (num <= 500):
    print(f'Raiz de {num}: {result: ,.2f}')

else:
    print('O número tem que ser menor que 500 :/')