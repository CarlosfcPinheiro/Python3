#Country position

countries = ("Brasil", "Estados Unidos", "Canada", "Japão", "Singapura")

print(f"Lista de países: {countries}")
while True:
    resp = int(input("Digite a posição de um país da lista: "))
    if (resp < len(countries) + 1) and (resp > 0):
        print(f"\nO país nessa posição é: {countries[resp - 1]}")
        break
    else:
        continue
    