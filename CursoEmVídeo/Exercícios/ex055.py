#Maior e Menor peso


larger = 0
smaller = 0
for c in range(1, 6):
    weight = float(input('Informe o peso da {0}º pessoa: '.format(c)).strip())
    if c == 1:
        larger = weight
        smaller = weight
    else:
        if weight > larger:
            larger = weight
        elif weight < smaller:
            smaller = weight
print(' ')
print('O \033[0;34mMAIOR\033[0m peso dentro os 5 é: {0}Kg'.format(larger))
print('E o \033[0;31mMENOR\033[0m peso dentre os 5 é: {0}Kg'.format(smaller))