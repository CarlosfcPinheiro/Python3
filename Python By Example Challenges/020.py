#Lenght of your name

name = str(input('Digite o seu nome: ').strip(' ').upper())

print(f'\nO nome {name} possui {len(name.replace(" ", ""))} letras.')