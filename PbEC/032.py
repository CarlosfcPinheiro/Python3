#Cylinder

import math

radius = float(input('Dê o raio de um cilindro qualquer (cm): '))
depth = float(input('Agora, forneça a altura desse mesmo cilindro (cm): '))

volume = (math.pi * (radius**2))*depth
print(f'\nO volume desse cilindro é de: {volume:,.2f}cm³')
