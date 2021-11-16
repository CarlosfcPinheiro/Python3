#Irá receber o nome completo de uma pessoa e dizer seu primeiro e último nome

nome = str(input('Digite seu nome completo: ')).strip().title()
nomelista = nome.split()
print('Seu primeiro nome é: {0}'.format(nomelista[0]))
print('E seu Último nome é: {0}'.format(nomelista[len(nomelista) - 1]))
