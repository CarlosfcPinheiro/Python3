#Determinação de ano bissexto

ano = int(input('Digite o ano que você quer saber se é bissexto ou não: '))
bissexto = ano % 4
if (bissexto == 0):
    print('O ano informado É bissexto.')
else:
    print('O ano informado NÃO É bissexto.')