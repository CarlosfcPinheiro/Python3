#Determinação de ano bissexto
from datetime import date

ano = int(input('Digite o ano que você quer saber se é bissexto ou não (digite 0 para o ano atual): '))
if (ano == 0):
    ano = date.today().year
bissexto1 = ano % 4
bissexto2 = ano % 100
bissexto3 = ano % 400
if (bissexto1 == 0) and (bissexto2 != 0) or (bissexto3 == 0):
    print('O ano de {0}, É bissexto.'.format(ano))
else:
    print('O ano de {0}, NÃO É bissexto.'.format(ano))