#Dividindo em listas

nums = []
odd = []
even = []
print('=-'*20+'=')
while True:
    num = int(input('\nDigite um número para adicionar a uma lista: '))
    if num % 2 == 1:
        odd.append(num)
    elif num % 2 == 0:
        even.append(num)
    nums.append(num)
    cont = str(input('Deseja continuar [S=sim/N=não]? ').upper().strip()[0])
    if cont == 'S':
        continue
    elif cont == 'N':
        break
print('=-'*20+'=')
print(f'\nLISTA COMPLETA: {nums}')
print(f'NÚMEROS PARES: {even}')
print(f'NÚMEROS ÍMPARES: {odd}')

