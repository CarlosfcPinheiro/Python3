#Correct number

import random

pc = random.randint(1, 5)
num = int(input("Digite um número de 1 a 5: "))

if (num == pc):
    print("Bom trabalho! Você acertou :)")

else:
    if (num > pc):
        print("\nEsse número foi mais alto. Tente mais uma vez")
    else:
        print("\nEsse número foi mais baixo. Tente mais uma vez.")
    num = int(input("Digite um outro número de 1 a 5: "))
    if (num == pc):
        print("\nParabéns! Agora você conseguiu.")
    else:
        print("\nNão foi dessa vez :(")