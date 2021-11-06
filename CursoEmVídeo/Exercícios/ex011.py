#Calcular a área de uma parede e saber qantos litros de tinta são precisos para pintá-la
h = float(input("Me diga a altura dessa parede (em metros): "))
l = float(input("Agora me diga a largura dessa parede (em metros): "))
A = l*h
lt = A/2
print("Sabendo que cada litro de tinta consegue pintar 2m², e que sua parede tem {0}m². \n"
"Você irá precisar de {1} litros de tinta.".format(A, lt))




