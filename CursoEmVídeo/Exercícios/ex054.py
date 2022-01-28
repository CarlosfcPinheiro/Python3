#Grupo de Maioridade

from datetime import date

ofage = 0
minor = 0
today = date.today().year
for c in range(1, 8):
    year = (int(input('Informe em que ano a {0}° nasceu: '.format(c))))
    if today-year >= 18:
        ofage += 1
    else:
        minor += 1
print('Das 7 pessoas informadas, {0} são maiores de idade e {1} são menor de idade.'.format(ofage, minor))


