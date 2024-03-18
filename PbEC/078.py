#TV's programs

programs = ["Sessão da Tarde", "Jornal Nacional", "Novela", "Domingão"]

for c in programs:
    print(c)

name = str(input("\nDigite o nome de outro programa: ").strip().title())
while True:
    num = int(input("Diga em que posição da lista você quer que fique: "))
    if (num <= 5) and (num >= 0):
        break
    else:
        continue
programs.insert(num - 1, name)
print(f"Aqui está sua nova lista: {programs}")

