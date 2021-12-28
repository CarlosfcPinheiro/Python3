#Conversos de bases numéricas

num = int(input('Digite um número qualquer (inteiro): '))
print('''
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
''')
choice = int(input('Digite o número correspondente ao tipo de base que você deseja converter esse número: '))
if (choice == 1):
    binary = bin(num)
    print('Seu número convertido para binário, é: {0}'.format(binary[2:]))

elif (choice == 2):
    octal = oct(num)
    print('Seu número convertido para octal, é: {0}'.format(octal[2:]))

elif (choice == 3):
    hexade = hex(num)
    print('Seu número convertido para ehxadecimal, é: {0}'.format(hexade[2:]))

else:
    print('Opção inválida.')