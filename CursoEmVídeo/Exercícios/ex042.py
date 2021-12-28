#Analisando triângulos

s1 = float(input('Forneça o primero lado do triângulo: ').strip())
s2 = float(input('Forneça o segundo lado do triângulo: ').strip())
s3 = float(input('Forneça o terceiro lado do triângulo: ').strip())
if (s1 < s2 + s3) and (s2 < s3 + s1) and (s3 < s2 + s1):
    if (s1 == s2 == s3):
        print('Esse triângulo é EQUILÁTERO.')
    elif (s1 != s2 != s3 != s1):
        print('Esse triângulo é ESCALENO.')
    else:
        print('Esse triângulo é ISÓCELES.')

else:
    print('Perdão, com essas medidas não é possível formar um triângulo.')
