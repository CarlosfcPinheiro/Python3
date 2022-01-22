#Analisador Completo

namemanold = 'nobody'
agemanold = 0
smaller = 0
average = 0
mancount = 0
for c in range(1, 5):
    print('=-=-=-=-= {0}° PESSOA =-=-=-=-='.format(c))
    name = str(input('Informe o nome: ').strip().title())
    age = int(input('Informe a idade: ').strip())
    mf = str(input('Informe o sexo com [M/F]: ').strip().upper())
    average += age
    #MULHERES COM MENOS DE 20 ANOS
    if (age < 20) and (mf == 'F'):
        smaller += 1
    #HOMEM MAIS VELHO
    if (c == 1) and (mf == 'M'):
        agemanold = age
        namemanold = name
    elif (age > agemanold) and (mf == 'M'):
        agemanold = age
        namemanold = name
    #QUANTIDADE DE HOMENS
    if (mf == 'M'):
        mancount += 1
#CHECANDO CONTAGEM DE PESSOAS CADASTRADAS
if smaller == 0:
    smaller = 'NENHUMA'
if mancount == 0:
    namemanold = 'NENHUM'

print('\nMÉDIA DE IDADES: {0:.0f}'.format(average/4))
print('MULEHRES COM MENOS DE 20 ANOS: {0}'.format(smaller))
print('NOME DO HOMEM MAIS VELHO: {0}'.format(namemanold))







