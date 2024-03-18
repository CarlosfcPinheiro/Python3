#Pig Latin

word = str(input('Digite uma palavra qualquer: ').strip())
vowel = ('a', 'e', 'i', 'o', 'u')

if (word[0] in vowel):
    print(f'\nPalavra em Pig Latin: {(word + "way").lower()}')

else:
    print(f'\nPalavra em Pig Latin: {(word + "ay").lower()}')