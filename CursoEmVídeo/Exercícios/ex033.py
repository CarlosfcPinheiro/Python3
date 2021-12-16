#Número maior e menor

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if (num1 > num2) and (num1 > num3):
    maior = num1
    print('O maior número dado foi {0}{1}{2}'.format('\033[0;34m', maior, '\033[m'))
if (num2 > num1) and (num2 > num3):
    maior = num2
    print('O maior número dado foi {0}{1}{2}'.format('\033[0;34m', maior, '\033[m'))
if (num3 > num1) and (num3 > num2):
    maior = num3
    print('O maior número dado foi {0}{1}{2}'.format('\033[0;34m', maior, '\033[m'))
if (num1 < num2) and (num1 < num3):
    menor = num1
    print('E o menor número foi {0}{1}'.format('\033[0;31m', menor))
if (num2 < num1) and (num2 < num3):
    menor = num2
    print('E o menor número foi {0}{1}'.format('\033[0;31m', menor))
if (num3 < num1) and (num3 < num2):
    menor = 3
    print('E o menor número foi {0}{1}'.format('\033[0;31m', menor))


