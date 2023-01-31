#Random array

from array import *
import random

array_nums = array ('i', [])
for c in range(0, 5):
    array_nums.append(random.randint(1, 100))

print("Seu array: ")
for i in array_nums:
    print(i)