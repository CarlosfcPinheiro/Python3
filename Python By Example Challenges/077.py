#Party.2

invites = []

for c in range(0, 3):
    name = str(input("Digite um nome para chamar para a festa: ").strip().title())
    invites.append(name)

while True:
    resp = str(input("\nDiga se você deseja chamar mais alguém: ").strip().upper())
    if (resp == "SIM"):
        name = str(input("Digite mais um nome para chamar para a festa: ").strip().title())
        invites.append(name)
        continue
    elif (resp == "NÃO") or (resp == "NAO"):
        print(f"Essa é a sua lista de convidados: {invites}")
        break
    else:
        continue

while True:
    name = str(input("\nDigite um nome da lista: ").strip().title())
    if (name in invites):
        print(f"A posição desse nome: {invites.index(name)}")
        while True:
            resp = str(input("\nVocê deseja excluir esse convite: ").strip().upper())
            if (resp == "SIM"):
                invites.remove(name)
                print(f"Essa é sua nova lista: {invites}")
                break
            elif (resp == "NÃO") or (resp == "NAO"):
                break
            else:
                continue
        break
    else:
        continue