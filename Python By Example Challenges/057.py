#Correct number.3

import random

pc = random.randint(1, 10)
num = int(input("Digite um número de 1 a 10: "))
print("")

while (num != pc):
    if (num > pc):
        num = int(input("Esse número é mais alto, digite outro: "))
    else:
        num = int(input("Esse número é mais baixo, digite outro: "))

print("\nParbéns! Você acertou o número.")