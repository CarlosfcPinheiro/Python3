#Irá receber 4 nomes e sortear uma ordem
from random import shuffle

nome1 = input('Qual o nome da primeira pessoa? ')
nome2 = input('Qual o nome da segunda pessoa? ')
nome3 = input('Qual o nome da terceira pessoa? ')
nome4 = input('Qual o nome da quarta pessoa? ')
pessoas = [nome1, nome2, nome3, nome4]
shuffle(pessoas)
print('A ordem aleatória das pessoas é:')
print(pessoas)