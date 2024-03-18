#Count Direction

direction = str(input("Diga se quer contar para CIMA ou para BAIXO: ").strip().upper())
if (direction == "CIMA"):
    num = int(input("Digite um número qualquer (positivo): "))
    if (num >= 1):
        for c in range(1, num+1):
            print(c)
        print("\nAcabou :)")
    else:
        print("Esse número é inválido.")
elif (direction == "BAIXO"):
    num = int(input("Digite um número abaixo de 20: "))
    if (num <= 20):
        for c in range(num, 0, -1):
            print(c)
        print("\nAcabou :)")
    else:
        print("Esse número é inválido.")   
else:
    print("Eu não entendi.")