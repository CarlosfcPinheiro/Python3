#Progressão Aritimética 3.0
from time import sleep

first = int(input('Digite o primeiro termo dessa P.A (Progressã Aritimética): '))
reason = int(input('Agora, digite a razão dessa P.A: '))
yellow = '\033[0;33m'
red = '\033[0;31m'
count = 1
all = 0
more = 10
while more != 0:
    all += more
    while count != all:
        print('{0}{1} - '.format(yellow, first), end='')
        first += reason
        count += 1
    print('PAUSA')
    more = int(input('{0}Se você deseja ver mais termos dessta P.A, digite quantos (se não, digite 0): '.format(red)))
print('Calculando dados...')
sleep(3)
print('Você viu um total de {0} termos dessa P.A :)'.format(all))




