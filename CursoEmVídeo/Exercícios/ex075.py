#Análise de Tupla

num1 = int(input('Digite um valor entre 1 e 10: '))
num2 = int(input('Digite outro valor entre 1 e 10: '))
num3 = int(input('Digite outro valor entre 1 e 10: '))
num4 = int(input('Digite um último valor entre 1 e 10: '))
nums = (num1, num2, num3, num4)
print(f'\033[0;33m\nNÚMERO DE VEZES QUE O 9 APARECEU:\033[0m {nums.count(9)}')
if 3 in nums:
    print(f'\033[0;33mPOSIÇÃO DO NÚMERO 3:\033[0m {nums.index(3)+1}° posição')
else:
    print('nenhum')
print('\033[0;33mNÚMEROS PARES DA TUPLA: \033[0m', end='')
count = 0
for n in nums:
    if (n % 2 ==0):
        print(n, end=' ')
        count += 1
    elif count == 0:
        print('nenhum')
        break
