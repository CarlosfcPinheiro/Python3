#Características de um caractere
x = input('Digite um caractere:')
print('O tipo primitivo desse caractere:', type(x))
print('O seu caractére é um número?', x.isnumeric())
print('O seu caractere é uma letra?', x.isalpha())
print('O seu caractere é um número e uma letra?', x.isalnum())
print('O seu caractere está em maiúsculo?', x.isupper())
print('O seu caractere está em minúsculo?', x.islower())
print('O seu caractere está capitalizado?', x.istitle())
