#Count down

num = int(input("Digite um número menor que 50: "))

if (num <= 50) and (num >= 1):
    for c in range(num, -1, -1):
        print(c)
print("\nAcabou :)")