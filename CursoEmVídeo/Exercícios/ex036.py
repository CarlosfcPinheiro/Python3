#Aprovador de empréstimo bancário para compra de uma casa

value = float(input('Me forneça o valor total da casa: '))
wage = float(input('Agora, me forneça o seu salário mensal: '))
years = int(input('Por último, diga por quantos anos você irá pagar a casa: '))
installment = value/(years * 12)
percentage = (wage * 30)/100
if (percentage > installment):
    print('\033[0;34mO valor de prestação da casa NÃO EXCEDE 30% do seu salário. O empréstimo foi aceito.')
else:
    print('\033[0;31mO valor de prestação EXCEDE 30% do seu salário. O empréstimo foi negado.')

