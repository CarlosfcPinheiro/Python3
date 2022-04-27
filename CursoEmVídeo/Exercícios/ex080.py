#Lista Ordenada sem usar o sort

nums = []
for c in range(0, 5):
    num = int(input('Digite um número para adicionar a lista: '))
    if c == 0 or num > nums[-1]:
        nums.append(num)
    else:
        for v in range(0, 5):
            if num <= nums[v]:
                nums.insert(v, num)
                break
print(f'\nLISTA FORMADA: {nums}')

