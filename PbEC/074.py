#Colors

colors = ["Azul", "Verde", "Vermelho", "Preto", "Roxo", "Amarelo", "Marrom", "Branco", "Lilás", "Ciano"]

while True:
    num1 = int(input("Digite um número de 0 a 4: "))
    if (num1 <= 4) and (num1 >= 0):
        break
    else:
        continue
while True:
    num2 = int(input("Agora, digite um número entre 5 e 9: "))
    if (num2 <= 9) and (num2 >= 5):
        break
    else:
        continue
print(f"\nPrimeira lista: {colors[0:num1]}")
print(f"Segunda lista: {colors[0:num2]}")