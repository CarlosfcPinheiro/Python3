#Analisando informações para alistamento

gender = str(input('Informe o seu sexo com M(masculino) ou F(feminino): ').upper())
if (gender == 'F'):
    print('Você não precisa se alistar.')
if (gender == 'M'):
    age = int(input('Informe quantos anos você possui: '))
    if (age == 18):
        print('Você está na hora de se alistar')
    elif (age > 18):
        time = age - 18
        print('Você já poderia ter se alistado à {0} ano(s)'.format(time))
    else:
        time = 18 - age
        print('Você ainda não pode se alistar, faltam {0} ano(s)'.format(time))