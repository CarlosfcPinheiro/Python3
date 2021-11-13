#Calcula a hipotenusa com base nos dados recebidos do cateto oposto e adjacente
from math import hypot

catop = float(input('Me dê os valores do cateto oposto (em metros): '))
catad = float(input('Me dê os valores do cateto adjacente (em metros): '))
hipo = hypot(catop, catad)
print('De acordo com os catetos fornecidos:\n'
      'cateto oposto = {0}m\n'
      'cateto adjacente = {1}m\n'
      'O valor da hipotenusa desse triângulo equivale a {2}m'.format(catop, catad, hipo))