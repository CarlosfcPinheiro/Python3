#Irá ler um número e mostrar sua porção inteira
from math import ceil

num = float(input('Digite um número REAL qualquer: '))
numint = ceil(num)
print('De acordo com o seu número dado, {0}\n'
      'Seu número como uma porção inteira é {1}'.format(num, numint))
