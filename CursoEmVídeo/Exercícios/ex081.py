#Análise de uma lista

nums = []
five = False
print('=-'*20+'=')
while True:
    nums.append(int(input('\nDigite um número para adicionar a uma lista: ')))
    cont = str(input('Você deseja continuar [S=Sim/N=não]? ').upper().strip()[0])
    if cont == 'S':
        continue
    else:
        break
for c in nums:
    if c == 5:
        five = True
print('=-'*20+'=')
print(f'\nQUANTIDADE DE ELEMENTOS DA LISTA: {len(nums)}')
nums.sort(reverse=True)
print(f'LISTA EM ORDEM DECRESCENTE: {nums}')
print(f'VALOR ENCONTRADO NA LISTA: {five}')