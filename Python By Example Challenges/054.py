#Cara ou Coroa

import random

pc = random.choice(["CARA", "COROA"])
player = str(input("Você quer escolher CARA ou COROA: ").strip().upper())

while True:
    if (player == "CARA") or (player == "COROA"):
        break

    else:
        print("\nOpção inválida. Tente novamente.")
        player = str(input("Você quer escolher CARA ou COROA: ").strip().upper())
    
if (player == pc):
    print("\nParabéns! você ganhou :)")

else:
    print("\nQue pena, você perdeu :(")

