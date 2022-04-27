#Menor e Maior valores na lista

nums = []
upper = 0
lower = 0
for n in range(0, 5):
    nums.append(int(input('Digite um número para a lista: ')))
    if n == 0:
        upper = lower = nums[n]
    else:
        if nums[n] > upper:
            upper = nums[n]
        if nums[n] < lower:
            lower = nums[n]
print(f'''\nVALORES DADOS: {nums}
MAIOR VALOR: {upper}
MENOR VALOR: {lower}''')
