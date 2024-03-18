#First name and Surname

name = str(input("Digite seu primeiro nome: ").strip().title())
print(f"Esse é o tamanho do seu primeiro nome: {len(name)}")

surname = str(input("\nDigite seu sobrenome: ").strip().title())
print(f"Esse é o tamanho do so seu sobrenome: {len(surname)}")

print(f"\nNome completo: {name} {surname}")
print(f"Tamanho do nome completo: {len(name + surname)}")