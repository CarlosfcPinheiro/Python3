#Simulador de Caixa Eletrônico

print('=-'*20 + '=')
print('{:^41}'.format('CAIXA ELETRÔNICO'))
print('=-'*20 + '=')
value = int(input('Informe quanto você quer sacar: R$'))
total = value
ballot = 100
allballot = 0
while True:
    if total >= ballot:
        total -= ballot
        allballot += 1
    else:
        if allballot != 0:
            print(f'Você sacou {allballot} notas de R${ballot},00.')
        if ballot == 100:
            ballot = 50
        elif ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 5
        elif ballot == 5:
            ballot = 1
        allballot = 0
        if total == 0:
            break
