#Name and number, for loop

name = str(input("Digite seu nome: ").strip())
num = int(input("Agora digite um número menor que 10: "))

if (num <= 10):
    for c in range(0, num):
        print(name)

    print("\nAcabou :)")
else:
    print("")
    for c in range(0, 3):
        print("Muito alto x_x")