#O programa irá lhe perguntar que nota representa a cifra apresentada.

import random as rand

count = 0
right = 0
ciphersdic = {'A': 'La', 'B': 'Si', 'C': 'Do', 'D': 'Re', 'E': 'Mi', 'F': 'Fa', 'G': 'Sol'}
cipherslist = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
while count <= 9:
    cipher = rand.choice(cipherslist)
    n = str(input(f'\nQual nota representa a cifra \033[0;33m{cipher}\033[0m: ').title().strip())
    count += 1
    if ciphersdic.get(cipher) == n:
        right += 1
        print(f'\033[0;32mVocê ACERTOU!\033[0m A resposta é {ciphersdic.get(cipher)}')
    else:
        print(f'\033[0;31mVocê ERROU\033[0m. A resposta era {ciphersdic.get(cipher)}')
print(f'\nVocê acertou {right}/10')





