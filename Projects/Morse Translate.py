#Irá traduzir uma mensagem em morse que for digitada no terminal

morse_characters = {"A": ".-", "B": "-...", "C": ".-.-", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": ".--.", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."}

#Morse-character ou character-morse
print("""
Escolha a opção de tradução: 

[1] Morse-Caractere
[2] Caractere-Morse
""")
while True:
    resp = int(input("Insira o índice: "))
    if (resp == 1):
        print("")
        while True:
            morse_code = str(input("Digite o código: ").strip())
            if ("." in morse_code) or ("-" in morse_code):
                morse_letters = morse_code.split()

                print("Tradução: ", end="")
                for c in morse_letters:
                    for i in morse_characters:
                        if (c == morse_characters[i]):
                            print(i, end="")
                break

            else: 
                continue
        break

    elif (resp == 2):
        print("")
        mensage = str(input("Digite a mensagem: ").upper().strip())
        #separando as letras e armazenando em uma lista
        words = []
        for p in mensage:
            words.append(p)

        print("Tradução: ", end="")
        for c in words:
            for i in morse_characters:
                if (c == i):
                    print(morse_characters[i], end=" ")
        break
    
    else:
        continue