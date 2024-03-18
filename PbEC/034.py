#Square and Triangle area

import math

resp = int(input('''
1) Cículo
2) Triângulo
Digite o índice da figura que você deseja calcular a área: '''))

if (resp == 1):
    radius = float(input('\nForneça o raio do cículo(cm): '))
    area = math.pi*(radius**2)
    print(f'A área desse círculo vale: {area:,.2f}cm²')

elif (resp == 2):
    base = float(input('\nForneça a base do triângulo(cm): '))
    height = float(input('Agora, forneça a altura do triângulo(cm): '))
    area = (base*height)/2
    print(f'\nA área desse triângulo vale: {area:,.2f}cm²')

else:
    print('Essa opção é inválida.')