#Detector de números primos

divisible = 0
num = (int(input('Digite um número inteiro qualquer: ')))
print('\033[0;33m=-' * 100 + '=\033[0m')
for c in range(1,num + 1):
    if (num % c == 0):
        print('\033[0;34m', end=' ')
        divisible += 1
    else:
        print('\033[0;31m', end=' ')
    print(c, end=' ')
print(' ')
print('\033[0;33m=-' * 100 + '=\033[0m')
if (divisible == 2):
    print('Esse número só é divisível po 1 e por ele mesmo, portanto É PRIMO.')
else:
    print('Esse número foi dividido {0} vezes, portanto ele NÃO É PRIMO.'.format(divisible))
