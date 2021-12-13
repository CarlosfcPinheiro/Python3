#Simulando um radar eletrônico

velocity = float(input('Digite a velocidade de um veículo (em Km/h): '))
if (velocity > 80):
    print('A velocidade deste veículo foi maior que 80Km/h, portanto será multado.')
    valuepenalty = (velocity - 80)*7
    print('O valor cobrado pela multa será de: R${0}'.format(valuepenalty))
else:
    print('A velocidade deste veículo está de acordo com a norma exigida.')