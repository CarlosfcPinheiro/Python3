#Jogo de adivinhação de número
from random import randint

num = int(input('Digite um número (entre 0 e 5) que você acha que será escolhido: '))
numsecret = randint(0, 5)

if (num == numsecret):
    print('Parabéns, você acertou o número!')
    print('O número realmente era {0}'.format(num))
else:
    print('Não foi dessas vez')
    print('O número era {0}'.format(numsecret))

