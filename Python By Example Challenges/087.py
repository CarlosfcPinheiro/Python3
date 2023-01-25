#Reverse

word = str(input("Digite uma palavra qualquer: ").strip())
pos = len(word)

for c in word:
    pos -= 1
    print(word[pos])