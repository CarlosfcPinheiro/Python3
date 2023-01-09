#Lullaby

line = str(input('Digite um trecho de uma canção: ').strip().capitalize())
print(f'O tamanho da sua canção é de: {len(line)} caracteres')

n1 = int(input('\nDigite um número inicial: '))
n2 = int(input('Digite um número secundário: '))

print(f'\nO trecho que você selecionou é: {line[n1-1:n2-1]}')

