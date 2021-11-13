#Baseado em um dado ângulo, irá calcular o cosseno, seno e tangente
from math import cos, sin, tan, radians

angulo = float(input('Me dê o ângulo que será utilizado: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print('De acordo com o ângulo dado, {0}°\n'
      'Os valores do seno, cosseno e tangente, aproximadamente foram: \n'
      'Sen = {1:.2f}\n'
      'Cos = {2:.2f}\n'
      'Tan = {3:.2f}'.format(angulo, sen, cos, tg))

