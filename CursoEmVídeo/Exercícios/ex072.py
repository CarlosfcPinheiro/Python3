#Número por extenso

numbers = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    num = int(input('Digite um número: '))
    if num > 20 or num < 0:
        print('TENTE NOVAMENTE.')
        continue
    else:
        print(f'\033[0;34mSeu número por extenso é: {numbers[num]}\033[0m\n')
        cont = str(input('Você deseja continuar [S=sim/N=não]? ').upper().strip()[0])
        if cont == 'S':
            continue
        else:
            print('Programa encerrado.')
            break
