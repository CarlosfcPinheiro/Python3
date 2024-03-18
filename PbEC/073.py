#Food's Dictcionary

foods = {}
count = 1

for c in range(0, 5):
    food = str(input("Digite o nome de uma comida que você gosta (Não repita): ").strip().title())
    foods[count] = food
    count += 1

print(f"Essa é a lista de comidas: {foods}\n")

while True:
    resp = str(input("Diga se deseja remover alguma comida da lista: ").strip().upper())
    if (resp == "SIM"):
        while True:
            item = int(input("Digite a posição do qual quer excluir: "))
            if (item > 5) or (item < 1):
                continue
            else:
                del foods[item]
                break
    elif (resp == "NAO") or (resp == "NÃO"):
        print(f"Sua lista atualizada: {sorted(foods.values())}")
        break

    else:
        continue
            




