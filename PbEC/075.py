#Number's List

numbers = []

for c in range(0, 4):
    while True:
        num = int(input("Digite um número com 3 dígitos: "))
        if (num >= 100) and (num < 1000):
            numbers.append(num)
            break
        else:
            continue
print("")
for i in numbers:
    print(i)
print("")
numdigit = int(input("Digite um número da lista: "))
if (numdigit in numbers):
    print(f"O número {numdigit} está na posição {numbers.index(numdigit)}")

else:
    print("Esse número não está na lista.")
