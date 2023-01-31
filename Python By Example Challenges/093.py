#New array

from array import *

array_numbers = array('i', [])
for c in range(0, 5):
    num = int(input("Digite um número: "))
    array_numbers.append(num)

print(f"Esse é o seu array: {sorted(array_numbers)}")
while True:
    resp = int(input("\nDigite um número para excluir: "))
    if (resp in array_numbers):
        array_numbers.remove(resp)
        array_newnumbers = array('i', [])
        array_newnumbers.append(resp)
        print(f"Esse é o seu novo array: {sorted(array_newnumbers)}")
        break
    else:
        print("Esse número não pertenceu ao array.")
        continue
    