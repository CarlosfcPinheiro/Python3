#Calculando IMC
from math import pow

height = float(input('Informe sua altura(m): ').strip())
weight = float(input('Agora, informe seu peso(Kg): ').strip())
IMC = weight/(pow(height, 2))
if (IMC < 18.5):
    print('Você está ABAIXO DO PESO.')
elif (IMC < 25):
    print('Você está no PESO IDEAL.')
elif (IMC < 30):
    print('Você está com SOBREPESO.')
elif (IMC < 40):
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA')