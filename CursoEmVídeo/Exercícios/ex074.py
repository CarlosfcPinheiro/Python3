#Análise de Tupla Aleatória
import random as rd

nums = (rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10), rd.randint(1, 10))
print(f'Esses foram os números sorteados: {nums}')
print(f'\n\033[0;34mMAIOR NÚMERO: {max(nums)}\033[0m')
print(f'\033[0;31mMENOR NÚMERO: {min(nums)}\033[0m')
print(f'\033[0')

