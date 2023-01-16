#Total add

total = 0
while total < 50:
    num = int(input("Digite um número para adicionar: "))
    total += num
    if (total < 50):
        print(f"O total agora é: {total}\n")
        
    else:
        print(f"Você atigiu o total de 50!")
