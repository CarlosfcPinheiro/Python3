#Gerenciador de pagamentos

price = float(input('Digite aqui, o preço total das suas compras: '))
print('''Essas são as formas de pagamento:
[1] À vista (dinheiro/cheque) ---> 10% de desconto
[2] À vista no cartão         ---> 5% de desconto
[3] Parcelado em 2x           ---> preço formal
[4] Parcelado em 3x ou mais   ---> 20% de juros''')
option = int(input('Digite a opção desejada: ').strip())
if (option == 1):
    discount = price - ((price*10)/100)
    print('''Sendo sua escolha, à vista (DINHEIRO/CHEQUE).
    O valor sofreu 10% de desconto e passou a ser R${0}'''.format(discount))
elif (option == 2):
    discount = price - ((price*5)/100)
    print('''Sendo sua escolha, Á VISTA NO CARTÃO.
    O valor sofreu 5% de desconto e passou a ser R${0}'''.format(discount))
elif (option == 3):
    print('''Sendo sua escolha, PARCELADO EM 2x
    O valor não sofreu alteração, portanto continua sendo R${0}'''.format(price))
elif (option == 4):
    installments = int(input('Informe quantas vezes você deseja parcelar a compra: '))
    interest = ((price/installments)*20)/100
    wtinterest = (price/installments) + interest
    print('''Sendo sua escolha, PARCELADO EM 3x OU MAIS.
    O valor resultante por mês, com um juros de 20%, é de R${1}'''.format(installments, wtinterest))
else:
    print('Essa opção é inválida, tente novamente.')