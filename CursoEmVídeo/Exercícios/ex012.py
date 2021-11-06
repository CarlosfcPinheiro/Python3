#Preço de um produto baseado em um desconto de 5%
pa = float(input("Digite o preço do produto sem nenhum desconto: "))
des = pa*5/100
pd = pa - des
print("Sendo o seu preço original R$ {0}.\n"
      "Com o desconto de 5%, seu preço passou a ser R$ {1}".format(pa, pd))