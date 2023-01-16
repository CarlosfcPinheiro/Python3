#Green bottles song

bottles = 10

while (bottles != 0):
    print(f"""\n 
    Há {bottles} garrafas verdes apoiadas na parede,
    {bottles} apoiadas na parede,
    e se uma acidentalmente caísse?\n""")
    bottles -= 1
    resp = int(input("Então me diga quantas garrafas iriam sobrar: "))

    if (resp == bottles):
        print("Isso! Você acertou...")

    else:
        while (resp != bottles):
            print("\nVocê errou, tente novamente :(")
            resp =int(input("Então me diga novamente, quantas garrafas iriam sobrar: "))
        print("Boa boa :)\n")