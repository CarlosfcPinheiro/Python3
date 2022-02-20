#Jogo Ímpar ou Par
from random import randint
from time import sleep

print('\033[0;33m=-'*20 + '=')
print('{:^40}'.format('ÍMPAR OU PAR'))
print('=-'*20 + '=\033[0m')
pc = randint(1, 10)
victory = 0
while True:
    choice = int(input('\033[0;31mDigite um número de 1 a 10: '))
    if choice >= 10 or choice <= 1:
        print('Essa escolha não é permitida, apenas entre 1 e 10. Tente novamente :/')
        break
    eo = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    if (eo in 'P') or (eo in 'I'):
        sum = pc + choice
        print('ÍMPAR')
        sleep(1)
        print('OU')
        sleep(2)
        print('PAR')
        if (sum % 3 == 0) and (eo in 'I'):
            print(f'O número do computador foi {pc} e o seu foi {choice}, resultando em {sum}.')
            print('Portando...VOCÊ GANHOU! Parabéns :)\n')
            victory += 1
        elif (sum % 2 == 0) and (eo in 'P'):
            print(f'O número do computador foi {pc} e o seu foi {choice}, resuntando em {sum}.')
            print('Portanto...VOCÊ GANHOU! Parabéns :)\n')
            victory += 1
        else:
            print(f'O número do computador foi {pc} e o seu {choice}, resultando em {sum}.')
            print('Portanto...VOCÊ PERDEU.\n')
            print(f'VITÓRIAS: {victory}')
            break
    else:
        print('Essa opção de escolha é inválida. Tente novamente :/')
        break


