#Analisador de strings (nome completo de uma pessoa)

nome = input('Me diga seu nome completo: ').strip()
print('Esse é seu nome com letras maiúsculas: {0}'.format(nome.upper()))
print('Esse é o seu nome com letras minúsculas: {0}'.format(nome.lower()))
espacos = nome.count(' ')
caracteres = len(nome)
print('Essa é a quantidade de letras do seu nome: {0}'.format(caracteres - espacos))
nomes = nome.split()
print('Essa é a quantidade de letras do seu primeiro nome: {0}'.format(len(nomes[0])))

