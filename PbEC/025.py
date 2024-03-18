#First and surname.3

fn = str(input('Digite seu primeiro nome: ').strip())

if (len(fn) < 5):
    sn = str(input('Digite seu sobrenome: ').strip())
    fullname = fn.upper() + ' ' + sn.upper()
    print(f'\nNOME COMPLETO: {fullname}')

else:
    print(f'SEU NOME: {fn.lower()}')