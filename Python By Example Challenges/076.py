#Party

invites = []

for c in range(0, 3):
    name = str(input("Digite o nome de alguém para convidar para a festa: ").strip().title())
    invites.append(name)

while True:
    resp = str(input("\nDiga se você deseja convidar mais alguém: ").strip().upper())
    if (resp == "SIM"):
        name = str(input("Digite mais um nome para chamar para a festa: ").strip().title())
        invites.append(name)
        continue
    elif (resp == "NÃO") or (resp == "NAO"):
        print(f"\nEssa é a sua lista de convidados: {invites}")
        break
    else:
        continue
