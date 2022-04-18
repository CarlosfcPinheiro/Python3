#Tupla de Preços

products = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('=-'*20+'=')
print('TUPLA DE PRODUTOS'.center(40))
print('=-'*20+'=')
for p in products:
    if type(p) == str:
        size1 = len(p)
        points = '.'*(30 - size1)
        print(f'{p}{points}', end='')
    else:
        if p >= 10 and p<100:
            print(f'R$  {p:.2f}')
        elif p >= 100:
            print(f'R$ {p:.2f}')
        else:
            print(f'R$   {p:.2f}')
print('=-'*20+'=')