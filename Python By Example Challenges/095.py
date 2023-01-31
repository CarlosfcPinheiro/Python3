#'f' Array

import numpy

array_nums = numpy.array([90.53, 12.36, 87.69, 43.47, 77.31])

print(f"Array atual: {array_nums.round(2)}")
while True:
    num = int(input("Digite um número entre 2 e 5: "))
    if (num <= 5) and (num >= 2):
        array_nums = array_nums/num
        print(f"\nEsse agora é o array: {array_nums.round(2)}")
        break
    else:
        print("Número inválido. Tente novamente.")
        continue
