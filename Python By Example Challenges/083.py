#Is upper

while True:
    word = str(input("Digite uma palavra em maiúsculo: ").strip())
    if (word.isupper() == True):
        print("Obrigado :)")
        break
    elif (word.islower() == True):
        continue
    else:
        print("Isso não atende a nenhum dos casos.")
        break
