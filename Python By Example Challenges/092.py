#Two arrays

from array import *
import random

array_random = array('i', [])
for c in range(0, 5):
    array_random.append(random.randint(1, 100))

array_numbers = array('i', [])
for i in range(0, 5):
    num = int(input("Digite um número: "))
    array_numbers.append(num)

array_numbers.extend(array_random)

print("\nEsse é o seu array atual:")
for a in sorted(array_numbers):
    print(a)
