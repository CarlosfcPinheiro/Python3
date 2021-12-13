#Número maior e menor

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if (num1 > num2) and (num1 > num3):
    print('O maior número é {0}'.format(num1))
if (num2 > num1) and (num2 > num2):
    print('O maior número é {0}'.format(num2))
if (num3 > num1) and (num3 > num3):
    print('O maior número é {0}'.format(num3))
if (num1 < num2) and (num1 < num3):
    print('E o menor número é {0}'.format(num1))
if (num2 < num1) and (num2 < num3):
    print('E o menor número é {0}'.format(num2))
if (num3 < num1) and (num3 < num2):
    print('E o menor número é {0}'.format(num3))

