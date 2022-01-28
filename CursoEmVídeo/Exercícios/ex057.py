#Validação de Dados (Masculino ou Feminino)

MoF = ''
mf = str(input('Informe seu sexo com M (MASCULINO) ou F (FEMININO): ')).upper()[0].strip()
if mf == 'M':
    MoF = '[MASCULINO]'
else:
    MoF = '[FEMININO]'
while mf not in 'MF':
    print('Perdão, esse dado é inválido tente novamente...')
    mf = str(input('Informe seu sexo com M (MASCULINO) ou F (FEMININO): ')).upper()[0].strip()
    if mf == 'M':
        MoF = '[MASCULINO]'
    else:
        MoF = '[FEMININO]'
print('Agradecemos pela atenção. O sexo informado foi: {0} {1}'.format(mf, MoF))



