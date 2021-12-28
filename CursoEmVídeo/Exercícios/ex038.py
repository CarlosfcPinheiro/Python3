#Comparação de dois números

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if (num1 > num2):
    print('O número maior é {0}'.format(num1))
    print('E o menor número é {0}'.format(num2))
elif (num2 > num1):
    print('O maior número é {0}'.format(num2))
    print('E o menor número é {0}'.format(num1))
else:
    print('Os números {0} e {1} são iguais'.format(num1, num2))