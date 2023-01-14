#Party's name

peop = int(input("Digite a quantidade de pessoas que você irá chamar para a festa: "))

if (peop <= 10):
    for c in range(1, peop+1):
        name = str(input("Digite o nome da pessoa: ").strip())
        print(f"{name} foi convidado(a)!\n")
    print("Você chamou todas as pessoas :)")

else:
    print("Muitas pessoas x_x")