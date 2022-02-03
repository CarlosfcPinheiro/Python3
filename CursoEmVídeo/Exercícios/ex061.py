#Progressão Aritimética 2.0

first = int(input('Me forceça o PRIMEIRO NÚMERO dessa P.A (Progressão Aritimética): '))
reason = int(input('Agora me dê a RAZÃO dessa P.A: '))
count = 1
print('Essa são os 10 primeiros termos da sua P.A: ',end='')
while count != 11:
    count += 1
    print(' {0} - '.format(first), end='')
    first += reason
print('ACABOU')
