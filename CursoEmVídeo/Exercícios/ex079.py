#Analisando Valores de uma lista

nums = []
while True:
    num = int(input('\nDigite um número para adicionar a uma lista: '))
    if num not in nums:
        nums.append(num)
    else:
        print('ERRO. Números iguais não podem ser adicionados na lista.')
    cont = str(input('Você deseja continuar [S=sim/N=não]? ').upper().strip()[0])
    if cont == 'S':
        continue
    elif cont == 'N':
        break
    else:
        print('TENTE NOVAMENTE.')
        cont = str(input('Você deseja continuar [S=sim/N=não]? ').upper().strip()[0])
nums.sort()
print(f'ESSA É A SUA LISTA: {nums}')
