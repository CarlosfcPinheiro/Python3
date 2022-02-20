#Estatísticas em Produtos
from time import sleep

print('=-'*20 + '=')
print('{:^41}'.format('COMPRA ELETRÔNICA'))
print('=-'*20 + '=')
keep = 'S'
total = expensive = count = lower = 0
cheap = ''
while keep == 'S':
    count += 1
    product = str(input('Digite O NOME do seu produto: '))
    price = float(input('Digite O PREÇO deste produto: R$'))
    total += price
    keep = str(input('Continuar [S = Sim/N = Não]: ')).upper().strip()[0]
    while keep not in 'NS':
        keep = str(input('Continuar [S = Sim/N = Não]: ')).upper().strip()[0]
    print('-------------------------------------')
    if (count == 1) or (price < lower):
        lower = price
        cheap = product
    if price > 1000:
        expensive += 1
    if keep == 'N':
        print('Analisando dados...')
        sleep(3)
        print(f'\nPREÇO TOTAL: R${total}')
        print(f'QUANT. DE PRODUTOS ACIMA DE R$1000,00: {expensive}')
        print(f'O PRODUTO MAIS BARATO: {cheap.upper()}, custando {lower}')
        break
