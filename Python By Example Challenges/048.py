#Party with while loop

count = 0
resp = "S"

while ("S" in resp):
    name = str(input("Digite o nome da pessoa que você quer convidar: ")).capitalize()
    print(f"{name} foi convidado(a)!\n")
    count += 1

    resp = str(input("Diga se você quer adicionar mais alguém [S=sim/N=não]: ").strip().upper())
print(f"Você chamou: {count} pessoas :)")
