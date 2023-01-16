#How many letters have your name?

name = str(input('Digite seu nome: ').strip())
letters = 0

for i in name:
    letters += 1

print(f'Seu nome possui {letters} letras.')