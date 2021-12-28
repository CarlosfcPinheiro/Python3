#Classificando atletas
from time import sleep
from datetime import date

print('''De acordo com essa tabela, será classificado um atleta de acordo com os anos de experiência: 
[ Até 9 anos ]      ----> MIRIM
[ Até 14 anos ]     ----> INFANTIL
[ Até 19 anos ]     ----> JÚNIOR
[ Até 25 anos]      ----> SÊNIOR
[ Acima de 25 anos] ----> MASTER''')
name = str(input('Com base nisso, informe seu nome: ').title().strip())
year = int(input('Agora, forneça seu ano de nascimento ').strip())
age = (date.today().year) - year
if (age <= 9):
    level = 'MIRIM'
elif (age <= 14):
    level = 'INFANTIL'
elif (age <= 19):
    level = 'JÚNIOR'
elif (age <= 25):
    level = 'SÊNIOR'
else:
    level = 'MASTER'
print('Carregando seus dados...')
sleep(3)
print('''NOME: {0}
IDADE: {1}
CLASSIFICAÇÃO: {2}'''.format(name, age, level))