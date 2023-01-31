#First array

from array import *

array_nums = array('i', [])

for c in range(0, 5):
    num = int(input("Digite um número: "))
    array_nums.append(num)
print(f"Esse é seu array: {sorted(array_nums, reverse=True)}")

