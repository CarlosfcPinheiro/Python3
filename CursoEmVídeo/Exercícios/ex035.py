#Irá analisar 3 retas e dizer se é possível formar um triângulo.

s1 = float(input('Informe a primeira reta: '))
s2 = float(input('Informe a segunda reta: '))
s3 = float(input('Informe a terceira reta: '))
if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
    print('\033[0;34mDado os segmentos anteriores, É POSSÍVEL formar um triângulo.')
else:
    print('\033[0;31mDado os segmentos anteriores, NÃO É POSSÍVEL formar um triângulo.')




