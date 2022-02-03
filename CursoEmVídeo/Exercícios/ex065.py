#Tratamento de Valores 2.0
from time import sleep

count = sum = upper = lower = 0
num = int(input('Digite um número: '))
yn = str(input('Deseja continuar? [S = sim/N = não]: ')).strip().upper()
while (yn in 'S') or (yn in 'SIM'):
    count += 1
    sum += num
    num = int(input('Digite um número: '))
    yn = str(input('Deseja continuar? [S = sim/N = não]: ')).strip().upper()
    if count == 1:
        lower = upper = num
    else:
        if num > upper:
            upper = num
        elif num < lower:
            lower = num
#ANSWER CONDITIONS
if (yn not in 'S') and (yn not in 'N'):
    print('Essa resposta é inválida. Tente novamente.')
if (yn in 'N') or (yn in 'NAO'):
    print('\nCarregando Dados...')
    sleep(3)
    print('MÉDIA DOS VALORES: {0}'.format(sum/count))
    print('MAIOR VALOR: {0}'.format(upper))
    print('MENOR VALOR: {0}'.format(lower))
