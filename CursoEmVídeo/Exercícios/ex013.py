#Reajuste salarial de 15% de aumento
satual = float(input("Digite o seu salário atual: "))
aumento = satual*15/100
snovo = satual + aumento
print("Sendo seu salário atual o valor de R$ {0:.2f}\n"
      "Após o aumento de 15%, seu salário passou a ser de R$ {1:.2f}".format(satual, snovo))
