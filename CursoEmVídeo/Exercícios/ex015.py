#Irá calcular o gasto total por um carro que está sendo usado, a partir do km rodado e os dias usados
kmrodados = float(input('Diga quantos quilômetros você dirigiu com o carro: '))
tempouso = int(input('Agora me diga quantos dias você utilizou o carro: '))
gasto = (60 * tempouso) + (0.15 * kmrodados)
print('Sabendo que a cada Km rodado custa R$0.15 e que um dia com o carro custa R$60.00\n'
      'Você rodou {0:.2f}Km e utilizou o carro por {1} dias, então o preço a se pagar será R${2:.2f}'.format(kmrodados, tempouso, gasto))