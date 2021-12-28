#Aprovação ou reprovação de um aluno

grade1 = float(input('Informe a sua primeira nota em um dado bimestre: '))
grade2 = float(input('Informe a sua segunda nota nesse mesmo bimestre: '))
average = (grade1 + grade2)/2
if (average > 7.0):
    print('\033[0;34mCom média {0}, esse aluno(você) foi APROVADO!'.format(average))
elif (average > 5.0) and (average < 6.9):
    print('\033[0;33mCom média {0}, esse aluno(você) está de RECUPERAÇÃO.'.format(average))
else:
    print('\033[0;31mCom média {0}, esse aluno(você) está REPROVADO.'.format(average))
