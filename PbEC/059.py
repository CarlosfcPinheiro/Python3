#Correct color

import random

color = random.choice(["AZUL", "VERMELHO", "AMARELO", "MARROM", "PRETO"])

while True:
    choose = str(input("Escolha entre as cores [Azul, Vermelho, Amarelo, Marrom, Preto]: ").strip().upper())

    if (choose == color):
        print("\nParabéns! Você acertou a cor :)")
        break
    
    else:
        if (color == "AZUL"):
            print("\nO céu é azul devido as substâncias gasosas presentes na atmosfera.\n")
            print("Agora, digite outra cor.")
        elif (color == "VERMELHO"):
            print("\nEm vestibulares, não é permitido o uso de caneta vermelha.\n")
            print("Agora, digite outra cor.")
        elif (color == "AMARELO"):
            print("\nO sol não é amarelo, apenas tem a luz branca dividida em outras cores pela atmosfera.\n")
            print("Agora, digite outra cor.")
        elif (color == "MARROM"):
            print("\nMuitos instrumentos de corda e arco são da cor marrom.\n")
            print("Agora, digite outra cor.")
        elif (color == "PRETO"):
            print("\nEm provas de vestibular, só são permitidas canetas pretas.\n")
            print("Agora digite outra cor.")
        else:
            print("Essa cor não é válida.\n")
            print("Agora, digite outra cor.")