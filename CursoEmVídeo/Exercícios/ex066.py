#Valores com Flag

print('Números serão pedidos, caso queria parar, digite 999: ')
num = sum = count = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    sum += num
    count += 1
print(f'A quantidade de NÚMEROS DIGITADOS (em exceção de 999): {count}')
print(f'A SOMA DOS NÚMEROS digitados (em exceção de 999) é de: {sum}')
