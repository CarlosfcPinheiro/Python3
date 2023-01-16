#Between 10 and 20

num = 0
while (num >= 20) or (num <= 10):
    num = int(input("Digite um número entre 10 e 20: "))
    if (num >= 20):
        print("\nEsse número é alto")
    elif (num <= 10):
        print("\nEsse número é baixo")

print("Obrigado :)")