#Informando casas decimais de um número (0 a 9999)

num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('A unidade desse número é: {0}'.format(unidade))
print('A dezena desse número é: {0}'.format(dezena))
print('A centena desse número é: {0}'.format(centena))
print('A milhar desse número é: {0}'.format(milhar))