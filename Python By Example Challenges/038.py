#Name by letter

name = str(input("Digite seu nome: ").strip())
num = int(input("Digite um número: "))

for c in range(0, num):
    for i in name:
        print(i)
    print("\n")
    
print("Acabou :)")