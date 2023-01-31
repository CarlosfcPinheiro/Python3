#Specif numbers array

from array import *

array_nums = array('i',[])
count = 0

while (count != 5):
    num = int(input("Digite um número: "))
    if (num >= 10) and (num <= 20):
        count += 1
        array_nums.append(num)
        
    elif (num > 20):
        print("Número muito alto.\n")

    else:
        print("Muito baixo.\n")

print("\nObrigado :)")