#Contando Vogais em uma Tupla

words = ('aprender', 'programar', 'linguagem', 'python', 'javascript', 'trabalhar', 'pratical', 'mercado', 'futuro')
vowels = ('a', 'e', 'i', 'o', 'u')
for w in words:
    print(f'\nNa palavra \033[0;33m{w.upper()}\033[0m: ', end='')
    for v in vowels:
        if v in w:
            print('\033[0;31m'+v+'\033[0m', end=' ')

