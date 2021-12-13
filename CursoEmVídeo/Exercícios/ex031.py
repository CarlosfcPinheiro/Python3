#Preço total de uma viagem

distance = float(input('Informe a distnância, em KM, que será percorrida na sua viagem: '))
if (distance <= 200):
    price = distance * 0.50
    print('O preço da sua passagem é de R${0}'.format(price))
else:
    price = distance * 0.45
    print('O preço da sua passagem é de R${0}'.format(price))