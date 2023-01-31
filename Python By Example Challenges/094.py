#Array's item

from array import *

array_nums = array ('i', [1, 3, 5, 7, 11])

print(f"Array pré-estabelecido: {array_nums}")
while True:
    numselec = int(input("Digite um número pertencente ao array: "))
    if (numselec in array_nums):
        print(f"\nEssa é a possição desse número: {array_nums.index(numselec) + 1}")
        break
    else:
        continue