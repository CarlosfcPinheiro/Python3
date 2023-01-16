#Numbers add.2

total = 0
for c in range(0, 2):
    num = int(input("Digite um número: "))
    total += num

resp = 'S'
while ("S" in resp):
    resp = str(input("\nVocê deseja adicionar mais um número [S=sim/N=não]: ").strip().upper())
    if ("S" in resp):
        num = int(input("Digite um número: "))
        total += num
    elif ("N" in resp):
        print(f"Seu total: {total}")
        break
    else:
        print("\nNão entendi.")

