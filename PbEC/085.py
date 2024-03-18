#How many vowels

vowels = ["A", "E", "I", "O", "U"]
count = 0

name = str(input("Digite seu nome: ").strip().upper())
for c in name:
    if (c in vowels):
        count += 1
print(f"Quantidade de vogais: {count}")