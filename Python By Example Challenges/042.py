#Numbers add

total = 0
for c in range(0, 5):
    num = int(input("Digite um número: "))
    resp = str(input("Digite se deseja adicionar o número ao total [S = Sim e N = não]: ").strip().upper())
    if (resp == "S"):
        total += num
    elif (resp == "N"):
        print("")
        continue
    else:
        print("Resposta inválida. Será tomada como sim.")
        total += num
    print("")
    
print(f"\nEsse é o seu total: {total}")


