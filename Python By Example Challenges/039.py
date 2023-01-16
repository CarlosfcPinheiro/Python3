#Table

num = int(input("Digite um número entre 1 e 12: "))
print(f"\nEssa é a tabuada de {num}: ")

if (num > 12) or (num < 1):
    print("Esse número não está entre 1 e 12.")
else:
    for c in range(1, 13):
        print(f"{c} x {num} = {c*num}")

    print("\nAcabou :)")
