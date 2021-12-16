#Reajuste de salário de um funcionário

current = float(input('Me diga qual é o seu salário atual: '))
if (current > 1250.00):
    increase = (current * 10)/100
    new = increase + current
    print('\033[0;34mCotando com um aumento salarial de 10%, seu salário agora é de R${0}'.format(new))
else:
    increase = (current * 15)/100
    new = increase + current
    print('\033[0;34mContando com um aumento salarial de 15%, seu salário agora é de R${0}'.format(new))

