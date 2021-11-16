#Irá ler uma frase e mostrar informações sobre o texto

frase = str(input('Digite uma frase qualquer: ')).lower().strip()
print('A quantidade de letras "a" que aparecem na frase é: {0}'.format(frase.count('a')))
print('A posição da primeira letra "a" nessa frase é: {0}'.format(frase.find('a')+1))
print('A posição da última letra "a" nessa frase é: {0}'.format(frase.rfind('a')+1))


