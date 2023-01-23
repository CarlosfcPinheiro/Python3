#Number's List

numbers = []

for c in range(0, 3):
    num = int(input("Digite um número: "))
    numbers.append(num)
while True:
    resp = str(input("Você deseja manter o último número: ").strip().upper())
    if (resp == "NÃO") or (resp == "NAO"):
        numbers.pop(2)
        num = int(input("Digite um novo número para ser adicionado: "))
        numbers.append(num)
        print(f"\nEssa é a lista de números: {numbers}")
        break
    elif (resp == "SIM"):
        print(f"Essa é sua lista de números: {numbers}")
        break
    else:
        continue