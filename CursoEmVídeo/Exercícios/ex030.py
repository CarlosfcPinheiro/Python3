#Número Par ou Ímpar

num = int(input('Digite um número qualquer: '))
rest = num % 2
if (rest == 0):
    print('O número informado é PAR.')
else:
    print('O número informado é ÍMPAR.')