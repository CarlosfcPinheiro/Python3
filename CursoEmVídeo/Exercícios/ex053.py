#Palíndromo ou não

phrase = str(input('Digite uma frase/palavra: ').upper().strip())
phrase = ''.join(phrase.split())
invert = phrase[::-1]
print(' ')
if invert == phrase:
    print('Essa é a sua frase/palavra invertida: {0}'.format(invert))
    print('Sendo a mesma coisa quando escrita normalmente, ou seja, \033[0;32mÉ UM PALÍNDROMO\033[0m.')
else:
    print('Essa é a sua frase/palavra invertida: {0}'.format(invert))
    print('Ela é diferente quando escrita normalmente, ou seja, \033[0;31mNÃO É UM PALÍNDROMO\033[0m.')

