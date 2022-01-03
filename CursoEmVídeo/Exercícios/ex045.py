#Pedra, papel e tesoura

from random import choice
print('\033[0;34m   '+'=-'*20+'=')
print('    '+'{:^40}'.format('|JOKENPÔ|'))
print('    '+'=-'*20+'=\033[0m')
move = int(input('''Dentre as três escolhas, digite de acordo com o respectivo número
\033[0;30m[1] PEDRA\033[0m
\033[0;32m[2] PAPEL\033[0m
\033[0;31m[3] TESOURA\033[0m
Esolha: ''').strip())
possibilities = ['PEDRA', 'PAPEL', 'TESOURA']
movepc = choice(possibilities)
#SITUAÇÃO DE EMPATE GERAL
if (move == 1) and (movepc == 'PEDRA'):
    print('''(Sua escolha X Escolha da máquina)
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                   \033[0;30mPEDRA\033[0m x \033[0;30mPEDRA\033[0m 
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Os dois são iguais, portanto é um EMPATE.''')
elif (move == 2) and (movepc == 'PAPEL'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;32mPAPEL\033[0m x \033[0;32mPAPEL\033[0m 
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Os dois são iguais, portanto é um EMPATE.''')
elif (move == 3) and (movepc == 'TESOURA'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;31mTESOURA\033[0m x \033[0;31mTESOURA\033[0m 
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Os dois são iguais, portanto é um EMPATE.''')
#SITUAÇÕES DE VITÓRIA DO PLAYER
elif (move == 1) and (movepc == 'TESOURA'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                        \033[0;30mPEDRA\033[0m x \033[0;31TESOURA\033[0m
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Pedra ganha de tesoura, portanto VOCÊ GANHOU!''')
elif (move == 2) and (movepc == 'PEDRA'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;32mPAPEL\033[0m x \033[0;30PEDRA\033[0m 
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Papel ganha de pedra, portanto VOCÊ GANHOU!''')
elif (move == 3) and (movepc == 'PAPEL'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;31mTESOURA\033[0m x \033[0;32mPAPEL\033[0m 
        \033[0;34=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Tesoura vence de papel, portanto VOCÊ GANHOU!''')
#SITUAÇÕES DE DERROTA DO PLAYER
elif (move == 1) and (movepc == 'PAPEL'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;30mPEDRA\033[0m x \033[0;32mPAPEL\033[0m
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Pedra perde para papel, portanto é um VOCÊ PERDEU.''')
elif (move == 2) and (movepc == 'TESOURA'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;32mPAPEL\033[0m x \033[0;31mTESOURA\033[0m 
        \00[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Papel perde para tesoura, portanto VOCÊ PERDEU.''')
elif (move == 3) and (movepc == 'PEDRA'):
    print('''(Sua escolha X Escolha da máquina)
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
                       \033[0;31mTESOURA\033[0m x \033[0;30mPEDRA\033[0m 
        \033[0;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[0m
Tesoura perde para pedra, portanto VOCÊ PERDEU.''')

else:
    print('\033[0;31mPerdão, essa opção escolhida não existe.Por favor, Tente novamente.\033[0m')
