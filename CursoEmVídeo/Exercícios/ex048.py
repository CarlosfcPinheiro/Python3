#Soma ímpares múltiplos de três

sum = 0
count = 0
for c in range(1, 501, 2):
    if (c % 3 == 0):
        sum += c
        count += 1
print('A soma total de \033[0;31m{0}\033[0m os números ímpares múltiplos de três, entre  1 e 500 é: \033[0;34m{1}\033[0m'.format(count ,sum))
