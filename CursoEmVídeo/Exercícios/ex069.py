#Cadastro de Pessoas
from time import sleep

ofage = 0
woman = 0
man = 0
print('=-'*20 + '=')
print('{:^40}'.format('CADASTRO'))
print('=-'*20 + '=')
while True:
    age = int(input('Idade: '))
    mf = str(input('Masculino ou Feminino [M/F]: ')).upper().strip()[0]
    if age >= 18:
        ofage += 1
    if mf == 'M':
        man += 1
    if mf == 'F' and (age < 20):
        woman += 1
    if (mf not in 'M') and (mf not in 'F'):
        print('\nEssa opção é inválida. Tente novamente :/')
        break
    cont = str(input('\nSe deseja continuar, digite [Sim = S/Não = N]: ')).upper().strip()[0]
    if (cont == 'N'):
        print(f'\nMAIORES DE IDADE: {ofage}')
        print(f'HOMENS CADASTRADOS: {man}')
        print(f'MULHERES MENORES DE 20 ANOS: {woman}')
        break
    else:
        print('\nEssa opção é inválida. Tente novamente :/')
        break

