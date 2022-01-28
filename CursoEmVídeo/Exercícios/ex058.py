#Jogo de Adivinhação de Número 2.0
from random import randint
from time import sleep

print('\033[0;33m=-'*20 + '=\033[0m')
print('{:^52}'.format('\033[0;31mJOGO DE ADIVINHAÇÃO\033[0m'))
print('\033[0;33m=-'*20 + '=\033[0m')

attemps = 0
rand = randint(1, 10)
anwser = str(input('Deseja começar a jogar? \n')).strip().upper()[0]
if anwser == 'S':
    print('Vamos começar...')
    sleep(3)
    num = int(input('De 1 a 10, digite qual número você acha que estou pensando: '))
    if num == rand:
        print('\033[0;32mPARABÉNS! Você acertou na primeira tentativa, o número realmente era {0} :D\033[0m'.format(num))
    else:
        while num != rand:
            attemps += 1
            if rand > num:
                print('O número em que pensei é maior do que esse :P\n')
                num = int(input('Tente acertar novamente >:) : '))
            elif num > rand:
                print('O número em que pensei é menor do que esse :P\n')
                num = int(input('Tente acertar novamente >:) : '))
elif anwser == 'N':
    print('Que pena, podemos jogar outra hora :(')
    quit()
else:
    print('Desculpe, essa resposta não é válida :/')
    quit()
print('\033[0;32mPARABÉNS! Você conseguiu acertar!\033[0m\n')
print('carregando estatísticas...\n')
sleep(3)
print('NÚMERO DE ACERTO: {0}'.format(rand))
print('NÚMERO DE TENTATIVAS: {0}'.format(attemps))


