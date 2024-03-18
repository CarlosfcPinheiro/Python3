#School subjects

subjects = ["Física", "Matemática", "História", "Química", "Geografia", "Artes"]

print(f"Lista de matérias: {subjects}")
while True:
    resp = str(input("\nDiga se você gosta de todas essas matérias: ").strip().upper())
    if (resp == "NÃO") or (resp == "NAO"):
        while True:
            choice = str(input("Digite o nome de uma que você não gosta: ").strip().title())
            if (choice in subjects):
                subjects.remove(choice)
                break
            else:
                continue
    elif (resp == "SIM"):
        print(f"\nEssa é a lista de matérias que você gosta: {subjects}")
        break

    else:
        continue



