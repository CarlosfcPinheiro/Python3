#Soma dos pares

soma = 0
for count in range(1, 7):
    num = int(input('Digite o {0}° número inteiro: '.format(count)))
    if (num % 2 == 0):
        soma += num
print('A soma dos números pares informados foi {0}'.format(soma))