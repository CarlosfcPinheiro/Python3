#Tabuada 3.0
from time import sleep

num = 0
while num >= 0:
    count = 0
    num = int(input('Digite um número inteiro para ver sua tabuada: '))
    if num <= 0:
        print('\nEncerrando processo...')
        sleep(3)
        break
    print('=-'*20 + '=')
    while count != 10 and num >= 0:
        count += 1
        print(f'{num} x {count} = {num*count}')
    print('=-'*20 + '=')