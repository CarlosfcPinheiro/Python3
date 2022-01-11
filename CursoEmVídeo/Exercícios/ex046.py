#CONTAGEM REGRESSIVA PARA FOGOS DE ARTIFÍCIO
from time import sleep
counts = 11
for times in range (1, 11):
    counts -= 1
    print(counts)
    sleep(1)
print('Os fogos começam a ser estourados...')

