#Sport's list

sports = ["Futebol", "Natação"]

resp = str(input("Digite qual é seu esporte favorito: ").strip().title())
if (resp == sports[0]) or (resp == sports[1]):
    print(f"Essa é a lista de esportes: {sorted(sports)}")

else:
    sports.append(resp)
    print(f"Essa é a lista de esportes: {sorted(sports)}")
