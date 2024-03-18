#Poem

poem = """ 
Não pergunto ou me preocupo.
Se há culpa em meu coração;
Sei que te amo,
seja o que fores."""
print(f"{poem}\n")

while True:
    num1 = int(input("Escolha um número de começo: "))
    if (num1 < len(poem)) and (num1 >= 0):
        while True:
            num2 = int(input("Escolha um número de final: "))
            if (num2 < len(poem)) and (num2 > num1):
                print(f"\nEsse é o corte: ")
                print(poem[num1:num2])
                break
            else:
                continue
        break
    else:
        continue
