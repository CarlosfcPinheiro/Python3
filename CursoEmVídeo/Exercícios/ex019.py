#Irá receber o nome de 4 pessoas e sortear uma delas
from random import choice

nome1 = input('Me dê o primeiro nome: ')
nome2 = input('Me dê o segundo nome: ')
nome3 = input('Me dê o terceiro nome: ')
nome4 = input('Me dê o quarto nome: ')
pessoas = [nome1, nome2, nome3, nome4]
print('A pessoa sorteada foi: {0}'.format(choice(pessoas)))