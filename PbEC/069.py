#Countries Tuple

countries = ("Brasil", "Estados Unidos", "Canada", "Japão", "Singapura")

print(f"Lista de países: {countries}")
while True:
    resp = str(input("Escolha um dos países: ").strip().title())
    if (resp in countries):
        print(f"\nEsse é o index do país: {countries.index(resp) + 1}")
        break
    else:
        continue
