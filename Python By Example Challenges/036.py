#Name 'n' times

name = str(input('Digite seu nome: ').strip())
num = int(input('Digite um número: '))

print('\nSeu nome:')

for i in range(0, num):
    print(name)

print('\nAcabou :)')