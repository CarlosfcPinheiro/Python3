#Conversor de temperatura °Ceusius para °Fahrenheit
grauC = float(input('Digite a temperatura em °Ceusius que você deseja converter: '))
grauF = float((grauC * 9/5) + 35)
print('Sua medida dada em ºCeusius foi de: {0:.2f}°C \n'
      'Que convertida para °Fahrenheint equivale a: {1:.2f}°F'.format(grauC, grauF))

