#Equal numbers in array

from array import *

array_nums = array('i', [1, 2, 5, 7, 5])
for c in array_nums:
    print(c)

num = int(input("Digite um número: "))

if (array_nums.count(num) == 1):
    print("Esse número aparece uma vez na lista.")
elif (array_nums.count(num)> 1):
    print(f"Esse número aparece {array_nums.count(num)} vezes.")
else:
    print("Esse número não pertence ao array.")

