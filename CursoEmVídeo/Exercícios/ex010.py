#Conversor real para dollar
r = float(input('Digite uma quantia de dinheiro em real:'))
d = float(r//5.67)
print('R${} convertido para dollar é/aproximadamente US${}'.format(r, d))